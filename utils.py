import argparse
import sys
import os

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input file')
    return parser.parse_args()

def read_maze_from_input():
    args: list = get_arguments()

    # Check if the file exists
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