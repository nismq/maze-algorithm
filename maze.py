import utils
from collections import deque
import sys

class Cell:
    def __init__(self, col, row, steps_from_start, parent_cell=None):
        self.col = col
        self.row = row
        self.steps_from_start = steps_from_start
        self.parent_cell = parent_cell

    def print(self):
        print(f"({self.col},{self.row})")

    def to_string(self):
        return f"({self.col},{self.row})"
        

def solve_maze(max_steps: int) -> (Cell | None):
    try:
        start_position = find_start()
    except Exception:
        print(f"\nError: Did not find start")
        sys.exit(1)
        
    queue = deque()
    queue.append(start_position)
    visited = [start_position.to_string()]

    up = (0,-1)
    down = (0,1)
    left = (-1,0)
    right = (1,0)

    while queue:
        first_in_queue = queue[0]
        for direction in [up, down, left, right]:
            adjacent_cell = Cell(first_in_queue.col + direction[0], 
                                 first_in_queue.row + direction[1], 
                                 first_in_queue.steps_from_start + 1, 
                                 first_in_queue)
            if is_valid_move(adjacent_cell, visited, max_steps):
                if is_exit(adjacent_cell): 
                    return adjacent_cell
                queue.append(adjacent_cell)
                visited.append(adjacent_cell.to_string())
        queue.popleft()
    return None


def find_start():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '^':
                return Cell(col=x, row=y, steps_from_start=0)
    raise Exception()


def is_valid_move(cell: Cell, visited: list, max_steps: int) -> bool:
    # A move is valid when it:
    # - is within the maze boundaries, 
    # - is not a wall
    # - has not been visited already
    # - is not too far from the start
    try:
        if (maze[cell.row][cell.col] != '#' and 
            cell.to_string() not in visited and 
            cell.steps_from_start <= max_steps):
            return True
        else:
            return False
    except:
        return False


def is_exit(cell: Cell) -> bool:
    if maze[cell.row][cell.col] == 'E':
        return True
    else:
        return False


def mark_path(exit_cell: Cell):
    current_cell = exit_cell.parent_cell
    while current_cell.parent_cell != None:
        maze[current_cell.row][current_cell.col] = '+'
        current_cell = current_cell.parent_cell


def main():
    global maze
    maze = utils.read_maze_from_input()

    for max_steps in [20, 150, 200]:
        print(f'Trying to solve maze with maximum steps of {max_steps} ...',
              end=' ')
        exit_cell = solve_maze(max_steps)
        if exit_cell:
            print(f'Solution found with {exit_cell.steps_from_start} steps.')
            mark_path(exit_cell)
            utils.write_output_file(maze)
            utils.print_maze(maze)
            break
        else:
            print('Solution not found.')
            utils.write_output_file(None)


if __name__ == '__main__':
    main()