# Maze Solver Algorithm

This project implements a maze-solving algorithm using **Breadth-First Search (BFS)** to find the shortest path through a maze.

## How to Use

### Input
The maze is provided as a plain text file (.txt), where:
- `#`: Represents walls that cannot be passed through.
- ` ` (whitespace):  Represents open, movable space.
- `^`: The starting point of the maze.
- `E`: The exit or goal of the maze.

Example text file:
```
##########
#  #     E
# ## #####
# #      #
# #####  #
#^       #
##########
```

### Running the Script

Python version used during development: Python 3.11.1

Make sure you have python installed and then run the command below. Provide a text file as a command line option.

```
python maze.py -i example-maze.txt
```


### Output
If a solution is found, the script outputs a visual representation of the maze to the command line and to output.txt file. The shortest path will be marked with plus (`+`) characters.

Example output:
```
##########
#  #+++++E
# ##+#####
# # ++++ #
# #####+ #
#^++++++ #
##########
```