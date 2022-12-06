from collections import defaultdict

# Define environment (either test or input)
env = "test"
stack_file = env + "_stack.txt"
instruction_file = env + "_instructions.txt"

class Stacks:
  def __init__(self, in_file):
    # Stack properties:
    # stack_dict(dict: int->list): dictionary whose keys are stack number
    #   and values are the stacks (as lists)
    # stack_num(int): stack number of the largest stack
    self.stack_dict = defaultdict(list)
    self.stack_num = 0
    
    for line in in_file:
      # Get extract containers from each line
      # Container labels appear every 4 characters, starting at index 1
      line_list = line.strip('\n')[1::4]

      # Iterate through container labels, updating stack_list and stack_num
      for i, char in enumerate(line_list):
        if char != ' ':
          self.stack_num = max(i+1, self.stack_num)
          self.stack_dict[i+1].insert(0, char)

  # Method which performs moves
  def move(self, source, dest, num, switch_order):
    # Check if stack has enough containers to move
    if num > len(self.stack_dict[source]):
      raise Exception(f"Not enough elements in stack {source} to move")
    
    # Pull off top num containers of source stack
    self.stack_dict[source], moved_boxes = self.stack_dict[source][:-num], self.stack_dict[source][-num:]

    # Switch the order of the moving containers for Part 1, leave alone for Part 2
    if switch_order:
      moved_boxes = moved_boxes[::-1]

    # Put the containers on the destination stack
    self.stack_dict[dest].extend(moved_boxes)

  # Method to get message from stack configuration
  # Looks at top container of every stack
  def get_message(self):
    index = 1
    message = ""
    for i in range(1, self.stack_num+1):
      if len(self.stack_dict[i]) > 0:
        message += self.stack_dict[i][-1]
    return message
    
# Get Stacks for first part
with open(stack_file) as in_file:
  s_1 = Stacks(in_file)

# Get Stacks for second part
with open(stack_file) as in_file:
  s_2 = Stacks(in_file)


with open(instruction_file) as in_file:
  for line in in_file:

    # Extract numbers from each line
    line_inst = line.split(' ')
    num, source, dest = int(line_inst[1]), int(line_inst[3]), int(line_inst[5])

    # Perform moves for each part
    s_1.move(source, dest, num, True)
    s_2.move(source, dest, num, False)

print(f"Part 1: {s_1.get_message()}")
print(f"Part 2: {s_2.get_message()}")
