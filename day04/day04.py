import re

# Function which returns true if the intervals [first_begin, first_end]
# and [second_begin, second_end] overlap, and false if not
def overlaps(first_begin, first_end, second_begin, second_end):
  if first_begin <= second_begin:
    return second_begin <= first_end
  else:
    return first_begin <= second_end

with open('input.txt', 'r') as in_file:
  first_count = 0
  second_count = 0
  for line in in_file:
    # Get the start/endpoints of both intervals from the line
    first_begin, first_end, second_begin, second_end = map(int, re.split('\-|,', line.strip()))

    # Check if the second if contained in the first
    if first_begin <= second_begin and first_end >= second_end:
      first_count += 1
    
    # Check if the first is contained in the second
    elif first_begin >= second_begin and first_end <= second_end:
      first_count += 1
    
    # For part 2, check if the intervals overlap at all
    if overlaps(first_begin, first_end, second_begin, second_end):
      # print(first_begin, first_end, second_begin, second_end)
      second_count += 1
  
  print(f'First part: {first_count}')
  print(f'Second part: {second_count}')