from random import randint

class Node:
    def __init__(self, value=None, next_element=None):
        self.val = value
        self.next = next_element

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            returned = self.head.val
            self.head = self.head.next
            self.length -= 1
            return returned

    def not_empty(self):
        return bool(self.length)

    def top(self):
        return self.head.val

def random_maze_generator(r, c, P0, Pf):
    ROWS, COLS = r, c

    maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    seen = [[False for _ in range(COLS)] for _ in range(ROWS)]
    previous = [[(-1, -1) for _ in range(COLS)] for _ in range(ROWS)]

    S = Stack()
    S.insert(P0)

    while S.not_empty():
        x, y = S.pop()
        seen[x][y] = True

        if (x + 1 < ROWS) and maze[x + 1][y] == 1 and previous[x][y] != (x + 1, y):
            continue
        if (0 < x) and maze[x-1][y] == 1 and previous[x][y] != (x-1, y):
            continue
        if (y + 1 < COLS) and maze[x][y + 1] == 1 and previous[x][y] != (x, y + 1):
            continue
        if (y > 0) and maze[x][y-1] == 1 and previous[x][y] != (x, y-1):
            continue

        maze[x][y] = 1
        to_stack = []

        if (x + 1 < ROWS) and not seen[x + 1][y]:
            seen[x + 1][y] = True
            to_stack.append((x + 1, y))
            previous[x + 1][y] = (x, y)

        if (0 < x) and not seen[x-1][y]:
            seen[x-1][y] = True
            to_stack.append((x-1, y))
            previous[x-1][y] = (x, y)

        if (y + 1 < COLS) and not seen[x][y + 1]:
            seen[x][y + 1] = True
            to_stack.append((x, y + 1))
            previous[x][y + 1] = (x, y)

        if (y > 0) and not seen[x][y-1]:
            seen[x][y-1] = True
            to_stack.append((x, y-1))
            previous[x][y-1] = (x, y)

        pf_flag = False
        while to_stack:
            neighbour = to_stack.pop(randint(0, len(to_stack) - 1))
            if neighbour == Pf:
                pf_flag = True
            else:
                S.insert(neighbour)

        if pf_flag:
            S.insert(Pf)

    x0, y0 = P0
    xf, yf = Pf
    maze[x0][y0] = 2
    maze[xf][yf] = 3

    return maze
def display_maze_with_path(maze, path):
    symbols = {0: "▓", 1: "◌", 2: "S", 3: "E", -1: "◍"}  

    for row in maze:
        print(" ".join(symbols[cell] for cell in row))
        
def dfs(x, y, path, maze, Pf):
  if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] != 1:
      return False

  path.append((x, y))

  if (x, y) == Pf:
      return True

  maze[x][y] = -1

  if dfs(x + 1, y, path, maze, Pf) or dfs(x - 1, y, path, maze, Pf) or dfs(x, y + 1, path, maze, Pf) or dfs(x, y - 1, path, maze, Pf):
      return True

def find_path(maze, P0, Pf,path):
  dfs(P0[0], P0[1], path, maze, Pf)
  print(path)
  return path

if __name__ == "__main__":
    n = int(input("Enter the size of the maze (n x n): "))
    P0 = (0, 0)
    Pf = (n - 1, n - 1)
    maze = random_maze_generator(n, n, P0, Pf)

    while True:
        display_maze_with_path(maze, [])
        print("\nOptions:")
        print("1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the game")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            path=[]
            find_path(maze, P0, Pf,path)
            if len(path)>0:
                display_maze_with_path(maze, path)
            else:
                print("No path found.")

        elif choice == "2":
            maze = random_maze_generator(n, n, P0, Pf)

        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
