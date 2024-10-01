import argparse
import sys
import os

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, 
                        required=True, help='Path to the input file')
    return parser.parse_args()


def read_maze_from_input():
    args: list = get_arguments()
    input_file = args.input
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    print(f"Processing file: {input_file}")
    with open(input_file, "r") as f:
        maze: list = []
        for line in f:
            maze.append(list(line.rstrip()))
    return maze


def print_maze(maze):
    for row in maze:
        print("".join(row))


def write_output_file(maze):
    args: list = get_arguments()
    input_file = args.input
    with open("output.txt", "w") as outfile:
        if maze:
            for row in maze:
                row_joined = "".join(row)
                outfile.write(f"{row_joined}\n")
        else:
            outfile.write(f"Solution not found to {input_file}")
    return None