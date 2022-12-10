# Computer class which will execute commands in the list
# Properties:
# cycle (int): current cycle number
# register (int): register value
# command_duration (int): amount of time left in current command
# command_increment (int): amount to increment register once command executes
class Computer:
  def __init__(self):
    self.cycle = 1
    self.register = 1
    self.command_duration = 0
    self.command_increment = 0

  # Function to run program (for Part 1)
  # Returns sum of registers at cycle == 20 (mod 40), up to stop_cycle
  # Inputs:
  # program (file): file containing commands
  # stop_cycle (int): cycle at which to stop counting
  def run_program(self, program, stop_cycle):
    # Keep track of answer
    answer = 0

    # Carry out necessary number of cycles
    while self.cycle <= stop_cycle:
      
      # If there is no command occuring, queue up another one
      if self.command_duration == 0:
        command_list = program.readline().strip().split()

        # If we hit an empty line, there are not enough commands to fill enough cycles
        if len(command_list) == 0:
          print(f"Not enough commands to get to cycle {stop_cycle}")
          return
        
        # Queue add command
        if command_list[0] == 'addx':
          self.command_increment = int(command_list[1])
          self.command_duration = 2
        # Queue noop command
        else:
          self.command_duration = 1
    
      # If the cycle is == 20 (mod 40), add signal strength to answer
      if self.cycle % 40 == 20:
        answer += self.register * self.cycle

      # Tick command_duration down one
      self.command_duration -= 1

      # If the command_duration hits 0, execute the command
      if self.command_duration == 0:
        self.register += self.command_increment
        self.command_increment = 0
    
      # Increment cycle
      self.cycle += 1
    return answer

  # Function to draw screen (for Part 2)
  # Inputs:
  # program (file): file of commands
  # height (int): screen height
  # width (int): screen width
  def draw_screen(self, program, height, width):
    # Initialize screen
    screen = ""

    # Iterate through cycles (pixels)
    while self.cycle <= height * width:

      # If no command is queued, queue on
      # (same as run_program)
      if self.command_duration == 0:
        command_list = program.readline().strip().split()
        if len(command_list) == 0:
          return
        if command_list[0] == 'addx':
          self.command_increment = int(command_list[1])
          self.command_duration = 2
        else:
          self.command_duration = 1

      # If the sprite coordinate (register) is within 
      # one of the pixel being drawn, light up the pixel
      # Note: since the pixels are labeled starting on 0,
      # the horizontal position of the pixel being drawn
      # is given by (self.cycle - 1) % width
      if abs(self.register - ((self.cycle - 1)% width)) <= 1:
        screen += "#"
      else:
        screen += '.'

      # Insert carriage returns at the edge of the screen
      if self.cycle % width == 0:
        screen += '\n'

      # Same as run_program
      self.command_duration -= 1

      if self.command_duration == 0:
        self.register += self.command_increment
        self.command_increment = 0
      
      self.cycle += 1
    return screen
    
    

c_1 = Computer()
c_2 = Computer()
with open('input.txt', 'r') as in_file:
  print(f'Part 1: {c_1.run_program(in_file, 220)}')


with open('input.txt', 'r') as in_file:
  print(f'Part 2:\n{c_2.draw_screen(in_file, 6, 40)}')

