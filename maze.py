import utils
from collections import deque

maze: list = utils.read_maze_from_input()

class Cell:
    def __init__(self, col, row, parent=None):
        self.col = col
        self.row = row
        self.parent = parent

    def print(self):
        print("({},{})".format(self.col, self.row))

    def to_string(self):
        return "({},{})".format(self.col, self.row)

def main():
    goal = solve_maze()
    if goal:
        print('solved')
    find_path(goal)
    print_maze()

def print_maze():
    for row in maze:
        print("".join(row))

def solve_maze():
    start_position = find_start()
    queue = deque()
    queue.append(start_position)
    visited = [start_position.to_string()]

    up = Cell(0,-1), down = Cell(0,1), left = Cell(-1,0), right = Cell(1,0)

    max_iterations = 400
    iterations = 0
    while queue and iterations < max_iterations:
        iterations += 1
        print('Iterations {}'.format(iterations))
        print('First in queue:', queue[0].to_string())

        for move in [up, down, left, right]:
            next_move = Cell(queue[0].col + move.col, queue[0].row + move.row)
            if is_valid_move(next_move) and next_move.to_string() not in visited:
                print('valid')
                next_move.parent = queue[0]
                queue.append(next_move)
                visited.append(next_move.to_string())
                if maze[next_move.row][next_move.col] == 'E':
                    return next_move
        print('-----')
        queue.popleft()
    print(visited)
    return None

def find_start():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '^':
                return Cell(col=x,row=y)
    return None

def is_valid_move(pos: Cell):
    print('-----')
    try:
        pos.print()
        print(maze[pos.row][pos.col])
        if maze[pos.row][pos.col] != '#':
            return True
    except:
        print('error')
        return False
    print('false')
    return False

def find_path(goal_pos: Cell):
    path = []
    pos = goal_pos

    while pos.parent != None:
        path.append(pos.to_string())
        maze[pos.row][pos.col] = '+'
        pos = pos.parent
    print(path)

if __name__ == '__main__':
    main()