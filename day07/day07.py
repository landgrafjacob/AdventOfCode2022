# TreeNode class which will represent files/directories in our file system
# Properties:
# parent (TreeNode): the parent folder of the file/directory in the file system
# type (string): either 'f' for file or 'd' for directory
# name (string): the name of the file/directory
# size (int): the (total) size of the file/directory
# children (dict: str -> TreeNode): A dict representing the contents of a dir. 
#                                   key: name of file/dir, value: the actual TreeNode
class TreeNode:
  # init
  def __init__(self, node_type, name, size, parent):
    self.parent = parent
    self.type = node_type
    self.name = name
    self.size = size
    self.children = {}

  # Method to add child to directory.
  # If the child is a file, will update the size of 
  # the directory and all parent directories
  def add_child(self, node):
    self.children[node.name] = node

    if node.type == 'f':
      current_node = self
      while current_node is not None:
        current_node.size += node.size
        current_node = current_node.parent

# FileSystem class which represents the entire file system
# Properties:
# root (TreeNode): Root directory of file system
# current_node (TreeNode): The current directory in the command line
class FileSystem:
  # Init
  def __init__(self, in_file):
    # Create node representing the root, set as current
    self.root = TreeNode('d', '/', 0, None)
    self.current_node = self.root

    # Track when an 'ls' command has been run
    listing = False

    for line in in_file:
      command_list = line.strip().split()
      # If an 'ls' command has been run, create the resources being listed
      if listing:
        # Create a subdir in current dir
        if command_list[0] == "dir":
          new_node = TreeNode('d', command_list[1], 0, self.current_node)
          self.current_node.add_child(new_node)
          continue
        # Create a file in current dir
        elif command_list[0].isnumeric():
          new_node = TreeNode('f', command_list[1], int(command_list[0]), self.current_node)
          self.current_node.add_child(new_node)
          continue
        # If we run into a new command, turn listing off
        else:
          listing = False

      # If line is a command
      if command_list[0] == "$":

        # Change directory
        if command_list[1] == "cd":
          # Change to root
          if command_list[2] == "/":
            self.current_node = self.root
          # Change to parent dir of current dir
          elif command_list[2] == "..":
            self.current_node = self.current_node.parent
          # Change to subdir of current dir (if created already)
          elif command_list[2] in self.current_node.children:
            self.current_node = self.current_node.children[command_list[2]]
          # If the subdir has not been created, create it and move there
          else:
            new_node = TreeNode('d', command_list[2], 0, self.current_node)
            self.current_node.add_child(new_node)
            self.current_node = new_node

        # Begin listing dir contents
        elif command_list[1] == "ls":
          listing = True

  # Method to find sum of directories whose size is <= 100000 using BFS
  def sum_small_directories(self):
    # Create a queue with just the root
    queue = [self.root]
    result = 0
    while len(queue) > 0:
      # Pop node off the queue
      next_node = queue.pop()

      # If the node is a dir with size <= 100000,
      # add the size to result
      if next_node.size <= 100000:
        result += next_node.size

      # Push subdirs onto queue
      for child in next_node.children.values():
        if child.type == 'd':
          queue = [child] + queue
    return result

  # Method to find smallest dir we could delete to obtain 
  # space_required amount of free disk space using BFS
  def find_directory_to_remove(self, space_required):
    # Calculate the additional space we need to clear 
    # (given that the total space on disk is 70000000)
    space_to_clear = space_required - (70000000 - self.root.size)

    # Set up queue with root dir
    queue = [self.root]
    result = self.root
    while len(queue) > 0:
      # Pop dir off queue
      next_node = queue.pop()

      # If the node is big to clear enough space,
      # check if it is smaller than any such node found already,
      # and add its subdirs to the queue
      if next_node.size >= space_to_clear:
        if next_node.size <= result.size:
          result = next_node
        for child in next_node.children.values():
          if child.type == 'd':
            queue = [child] + queue

    return result

# Turn input file into a FileSystem object
with open('input.txt', 'r') as in_file:
  d = FileSystem(in_file)

print(f"Part 1: {d.sum_small_directories()}")
print(f"Part 2: {d.find_directory_to_remove(30000000).size}")
    