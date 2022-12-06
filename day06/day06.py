from collections import defaultdict

file_name = 'input.txt'


class Message:
  def __init__(self, message):
    self.message = message

  # Method which loops through message to find starting marker
  def get_starting_marker(self, marker_len):
    count_dict = defaultdict(int)

    # Initialize counting dictionary
    for i in range(marker_len):
      count_dict[self.message[i]] += 1

    # Set windows of length marker_len
    left_pointer = 0
    right_pointer = marker_len

    # Slide window along message, checking if all the letter counts
    # within the window are <= 1
    while right_pointer < len(line):
      # If all chars in window are distinct, return the right endpoint
      # of window
      if all(x <= 1 for x in count_dict.values()):
        return right_pointer

      # Slide window
      count_dict[line[left_pointer]] -= 1
      count_dict[line[right_pointer]] += 1
      left_pointer += 1
      right_pointer += 1


with open(file_name, 'r') as in_file:
  line = in_file.readline().strip()
  m = Message(line)

print(f"Part 1: {m.get_starting_marker(4)}")
print(f"Part 2: {m.get_starting_marker(14)}")