with open('input.txt', 'r') as in_file:
  tree_grid = list(map(lambda x : list(x.strip()), in_file.readlines()))

visibility_set = set()
height = len(tree_grid)
width = len(tree_grid[0])

################
#### Part 1 ####
################

# Check visibility from left
for i in range(height):
  tallest = -1
  for j in range(width):
    if int(tree_grid[i][j]) > tallest:
      visibility_set.add((i,j))
      tallest = int(tree_grid[i][j])

# Check visibility from top
for j in range(width):
  tallest = -1
  for i in range(height):
    if int(tree_grid[i][j]) > tallest:
      visibility_set.add((i,j))
      tallest = int(tree_grid[i][j])

# Check visibility from left
for i in range(height-1, -1, -1):
  tallest = -1
  for j in range(width-1, -1, -1):
    if int(tree_grid[i][j]) > tallest:
      visibility_set.add((i,j))
      tallest = int(tree_grid[i][j])

# Check visibility from bottom
for j in range(width-1, -1, -1):
  tallest = -1
  for i in range(height-1, -1, -1):
    if int(tree_grid[i][j]) > tallest:
      visibility_set.add((i,j))
      tallest = int(tree_grid[i][j])

print(f"Part 1: {len(visibility_set)}")

################
#### Part 2 ####
################

# Function to find the number of trees visible in a given direction from coordinates (i,j)
def visibility_length(i, j, direction, tree_grid):
  tree = int(tree_grid[i][j])

  # Step one unit in given direction
  distance = 1
  x = i + direction[0]
  y = j + direction[1]
  
  # Keep stepping until you hit a taller tree, or the end of the grid
  while x >= 0 and y >= 0 and x < len(tree_grid) and y < len(tree_grid[0]):
    if tree <= int(tree_grid[x][y]):
      return distance
    x += direction[0]
    y += direction[1]
    distance += 1
  # If you hit the end of the grid, you will have stepped one 
  # unit more than the number of trees you've seen
  return distance - 1

max_scenic_score = 0

for i in range(height):
  for j in range(width):
    scenic_score = 1
    # Calculate the visibility length in each direction (up, down, left, right)
    # from coordinate (i,j) and multiply them all together
    for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
      scenic_score *= visibility_length(i, j, direction, tree_grid)
    max_scenic_score = max(scenic_score, max_scenic_score)

print(f"Part 2: {max_scenic_score}")
