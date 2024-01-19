# Terminal_Based_Maze_Solver
## Overview
<p>The "Terminal Based Maze Solver" project is a Python implementation of a maze generation and solving algorithm. The project includes a maze generator that creates a random maze with a specified size and starting (S) and ending (E) points. Additionally, it features a depth-first search (DFS) algorithm to find a path from the starting point to the ending point in the generated maze. </p>

## Components
### Maze Generation
<p>The maze generation utilizes a stack-based algorithm to create a random maze. The algorithm ensures that there is only one path between the starting and ending points, making the maze solvable. The generated maze consists of cells marked as follows:

0: Wall(▓)
1: Open path(◌)
2: Starting point (S)
3: Ending point (E)
4: Path(◍)</p>

### Depth-First Search (DFS)
<p>The DFS algorithm is employed to find a path from the starting point to the ending point in the generated maze. The DFS explores possible paths, backtracking when necessary, until it successfully reaches the destination. The path is then displayed, and the maze with the path is printed.</p>

### User Interaction
<p>The user can interact with the program through a simple console interface with the following options:

1. Print the Path: Display the solution path in the generated maze.
2. Generate Another Puzzle: Create a new random maze.
3. Exit the Game: Terminate the program.</p>

## Clone repository from github

- bash git clone
```https://github.com/kumarroshan123/Terminal_Based_Maze_Solver.git ```

## How to Run
<p>To run the program, execute the Python script. Upon launching, the user will be prompted to enter the size of the maze. The program will then display the maze and provide options for interacting with the generated puzzle.</p>

## Dependencies
<p>The project has no external dependencies beyond the standard Python library.</p>

## Additional Notes

1. The maze generator ensures that there is a solvable path from the starting point to the ending point.
2. The DFS algorithm employs a recursive approach to explore possible paths within the maze.
3. The solution path is marked with a different symbol ("-1") in the displayed maze.


## Output_Screenshots
![Screenshot 2024-01-17 233755](https://github.com/kumarroshan123/Terminal_Based_Maze_Solver/assets/76846167/4d838b93-abc4-438b-9d7c-74360bfd680a)
![Screenshot 2024-01-17 234115](https://github.com/kumarroshan123/Terminal_Based_Maze_Solver/assets/76846167/3af06b1f-139f-4a39-aad4-9d3fdf5fdf09)
