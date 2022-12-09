# Dict mapping directions to vectors
direction_dict = {
  "L": (-1, 0),
  "R": (1, 0),
  "U": (0, 1),
  "D": (0, -1)
}

# Class representing the knots in the rope
# Properties:
# x (int): x-coordinate of knot
# y (int): y-coordinate of knot
# parent (Knot): parent knot (one closer to the head knot)
# child (Knot): child knot (one further from head knot)
class Knot:
  def __init__(self, parent):
    self.x = 0
    self.y = 0
    self.parent = parent
    self.child = None

  # Method to add child to knot
  def add_child(self, knot):
    self.child = knot

  # Method to move a knot
  # Returns the position of the tail knot (as a tuple)
  def move(self, direction):
    # If the knot is the head knot, move in specified direction
    # and move child knots accordingly
    if self.parent is None:
      self.x += direction[0]
      self.y += direction[1]
      if self.child is None:
        return (self.x, self.y)
      else:
        return self.child.move(None)

    # If the knot is not the head, calculate the vector 
    # between it and its parent knot
    x_dist = abs(self.x - self.parent.x)
    y_dist = abs(self.y - self.parent.y)

    # If the x-coords differ by 2 and y-coords differ by 1,
    # move knot diagonally
    # Example case:
    # ...     ...   
    # ..H --> .TH
    # T..     ...
    if x_dist == 2 and y_dist == 1:
      self.x = (self.x + self.parent.x) // 2
      self.y = self.parent.y

    # Similar to previous case
    elif x_dist == 1 and y_dist == 2:
      self.y = (self.y + self.parent.y) // 2
      self.x = self.parent.x

    # If the x-coords or y-coords (or both) differ by two,
    # move knot to midpoint between knot and its parent
    # Example case:
    # ...     ...   
    # T.H --> .TH
    # ...     ...
    #
    # Example case:
    # ..H     ..H   
    # ... --> .T.
    # T..     ...
    elif (x_dist, y_dist) in [(0,2), (2,0), (2,2)]:
      self.x = (self.x + self.parent.x) // 2
      self.y = (self.y + self.parent.y) // 2

    # If the knot is the tail, return its coords,
    # otherwise, move its child not
    if self.child is None:
      return (self.x, self.y)
    else:
      return self.child.move(None)

# Class representing the whole rope (with given number of knots)
# Essentially a doubly linked list
# Properties:
# head (Knot): head knot of rope
# visited (list[tuple]): list of coordinates visited by tail
class Rope:
  # Initialize rope of given length
  def __init__(self, num):
    # Create head knot (with no parent)
    self.head = Knot(None)
    # Tail begins at coord (0,0)
    self.visited = {(0,0)}

    # Create num-1 more knots, adding them to end of rope
    current = self.head
    for _ in range(num-1):
      new_knot = Knot(current)
      current.add_child(new_knot)
      current = new_knot

  # Method to move head of rope (and all children knots),
  # and add the tail position to the visited set
  def move(self, direction):
    self.visited.add(self.head.move(direction))

# Initialize ropes
# 2 knots for part 1, 10 for part 2
r_1 = Rope(2)
r_2 = Rope(10)

# Follow given instructions
with open('input.txt', 'r') as in_file:
  for line in in_file:
    direction, distance = line.strip().split()
    for _ in range(int(distance)):
      r_1.move(direction_dict[direction])
      r_2.move(direction_dict[direction])

# Print number of coords visited by tails
print(f"Part 1: {len(r_1.visited)}")
print(f"Part 2: {len(r_2.visited)}")
