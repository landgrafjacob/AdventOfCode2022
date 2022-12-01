with open('input.txt', 'r') as in_file:
    cal_list = []
    running_total = 0
    for line in in_file:
        if line == '\n':
            cal_list.append(running_total)
            running_total = 0
        else:
            running_total += int(line.strip())
    cal_list.append(running_total)

    # Part 1
    print(f'Part 1: {max(cal_list)}')

    # Part 2
    print(f'Part 2: {sum(sorted(cal_list, reverse=True)[:3])}')

