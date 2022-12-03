# Given a letter, returns its priority
def char_to_num(char):
  ascii_val = ord(char)
  if ascii_val >= 97:
    return ascii_val - 96
  else:
    return ascii_val - 38

# Given a string representing contents of both
# compartments of bag, return the char in both 
# compartments
def find_common_char(line):
  left = 0
  right = len(line) - 1
  left_set = set()
  right_set = set()

  while left < right:
    if line[left] == line[right] or line[left] in right_set:
      return char_to_num(line[left])
    elif line[right] in left_set:
      return char_to_num(line[right])
    else:
      left_set.add(line[left])
      right_set.add(line[right])
      left += 1
      right -= 1

# Given running_set, line, and line_num, returns the
# characters in line that are in line_num, as well as the 
# priority of the last remaining letter at the end of the 
# 3-line chunk.
def find_in_consec_lines(running_set, line, line_num):
  if line_num == 0:
    return set(line), 0
  elif line_num == 1:
    return {s for s in line.strip() if s in running_set}, 0
  else: 
    return set(), char_to_num(next(iter({s for s in line.strip() if s in running_set})))

first_result = 0
second_result = 0

with open('input.txt', 'r') as in_file:
  line_num = 0
  running_set = set()
  temp_set = set()
  for line in in_file:
    first_result += find_common_char(line.strip())
    running_set, increment = find_in_consec_lines(running_set, line, line_num)
    second_result += increment
    line_num = (line_num + 1) % 3

    
print(f'First part: {first_result}')
print(f'Second part: {second_result}')


