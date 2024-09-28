import utils
from collections import deque

class Pos:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def print(self):
        print("({},{})".format(self.x, self.y))

    def to_string(self):
        return "({},{})".format(self.x, self.y)

def main():
    maze: list = utils.read_maze_from_input()
    goal = solve_maze(maze)
    if goal:
        print('solved')
    find_path(maze, goal)
    print_maze(maze)


def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze):
    start_position = find_start(maze)
    queue = deque()
    queue.append(start_position)
    visited = [start_position.to_string()]

    up = Pos(0,-1)
    down = Pos(0,1)
    left = Pos(-1,0)
    right = Pos(1,0)

    print(start_position)

    max_iterations = 400
    iterations = 0
    while queue and iterations < max_iterations:
        iterations += 1
        print('Iterations {}'.format(iterations))
        print('First in queue:', queue[0].to_string())
        for move in [up, down, left, right]:
            next_move = Pos(queue[0].x + move.x, queue[0].y + move.y)
            if is_valid_move(maze, next_move) and next_move.to_string() not in visited:
                print('valid')
                next_move.parent = queue[0]
                queue.append(next_move)
                visited.append(next_move.to_string())
                if maze[next_move.y][next_move.x] == 'E':
                    return next_move
        print('-----')
        queue.popleft()
    print(visited)
    return None

def find_start(maze: list):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '^':
                return Pos(x,y)
    return None

def is_valid_move(maze: list, pos: Pos):
    print('-----')
    try:
        pos.print()
        print(maze[pos.y][pos.x])
        if maze[pos.y][pos.x] != '#':
            return True
    except:
        print('error')
        return False
    print('false')
    return False

def find_path(maze: list, goal_pos: Pos):
    path = []
    pos = goal_pos

    while pos.parent != None:
        path.append(pos.to_string())
        maze[pos.y][pos.x] = '+'
        pos = pos.parent
    print(path)

if __name__ == '__main__':
    main()