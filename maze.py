import utils
from collections import deque

maze: list = utils.read_maze_from_input()

class Cell:
    def __init__(self, col, row, steps_from_start=None, parent_cell=None):
        self.col = col
        self.row = row
        self.steps_from_start = steps_from_start
        self.parent_cell = parent_cell

    def print(self):
        print(f"({self.col},{self.row})")

    def to_string(self):
        return f"({self.col},{self.row})"
        

def solve_maze(max_steps: int) -> (Cell | None):
    start_position = find_start()
    start_position.steps_from_start = 0
    queue = deque()
    queue.append(start_position)
    visited = [start_position.to_string()]

    up = (0,-1)
    down = (0,1)
    left = (-1,0)
    right = (1,0)

    max_iterations = 400
    iterations = 0
    while queue and iterations < max_iterations:
        iterations += 1

        for move in [up, down, left, right]:
            next_move = Cell(queue[0].col + move[0], queue[0].row + move[1])
            if is_valid_move(next_move, visited):
                next_move.parent_cell = queue[0]
                next_move.steps_from_start = queue[0].steps_from_start + 1
                if next_move.steps_from_start > max_steps:
                    return None
                queue.append(next_move)
                visited.append(next_move.to_string())
                if maze[next_move.row][next_move.col] == 'E':
                    return next_move
        queue.popleft()
    return None


def find_start():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '^':
                return Cell(col=x,row=y)
    return None


def is_valid_move(cell: Cell, visited: list):
    try:
        if maze[cell.row][cell.col] != '#' and cell.to_string() not in visited:
            return True
    except:
        return False
    return False


def mark_path(exit_cell: Cell):
    path = []
    current_cell = exit_cell.parent_cell
    while current_cell.parent_cell != None:
        path.append(current_cell.to_string())
        maze[current_cell.row][current_cell.col] = '+'
        current_cell = current_cell.parent_cell


def main():
    for max_steps in [20, 150, 200]:
        print(f'Trying to solve maze with maximum steps of {max_steps} ...', end=' ')
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