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

    def get_position(self):
        return f"(row:{self.row}, col:{self.col})"
        

def solve_maze(max_steps: int) -> (Cell | None):
    start_position = find_start()        
    queue = deque()
    queue.append(start_position)
    visited = [start_position.get_position()]

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
                visited.append(adjacent_cell.get_position())
        queue.popleft()
    raise Exception('Exit not found')


def find_start():
    try:
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == '^':
                    return Cell(col=x, row=y, steps_from_start=0)
        raise Exception
    except Exception:
        print(f"\nError: Did not find start")
        sys.exit(1)


def is_valid_move(cell: Cell, visited: list, max_steps: int) -> bool:
    # A move is valid when it:
    # - is a whitespace (' ') or exit ('E')
    # - is within the maze boundaries, 
    # - has not been visited already
    # - is not too far from the start

    expected_characters = ['#','^','E',' ']
    try:
        cell_value = maze[cell.row][cell.col]
        if cell_value not in expected_characters:
            raise ValueError(cell_value)
        if (cell_value != '#' and 
            cell.get_position() not in visited and 
            cell.steps_from_start <= max_steps):
            return True
        else:
            return False
    except IndexError:
        return False
    except ValueError as e:
        print(f"\nError: Unexpected character '{e}' at "
              f"line {cell.row + 1} column {cell.col + 1}")
        sys.exit(1)


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
        try:
            exit_cell = solve_maze(max_steps)
            print(f'Exit found with {exit_cell.steps_from_start} steps.')
            mark_path(exit_cell)
            utils.write_output_file(maze)
            utils.print_maze(maze)
            break
        except Exception as e:
            print(e)
            utils.write_output_file(None)


if __name__ == '__main__':
    main()