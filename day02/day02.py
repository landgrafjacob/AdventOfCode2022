# Dictionary converting shape to points
shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# Dictionary converting opponents play
# and our play into outcome points (part 1)
outcome_dict = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}

# Dictionary converting opponents play
# and result into shape points (part 2)
result_to_choice = {
    "A": {
        "X": 3,
        "Y": 1,
        "Z": 2
    },
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "C": {
        "X": 2,
        "Y": 3,
        "Z": 1
    }
}

# Dictionary converting result into outcome points
result_points = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

with open('input.txt', 'r') as in_file:
    first_score = 0
    second_score = 0
    for line in in_file:
        opp_move, my_move = line.strip().split(" ")
        first_score += shape_score[my_move] + outcome_dict[opp_move][my_move]
        second_score += result_points[my_move] + result_to_choice[opp_move][my_move]
    
    print(f'First part: {first_score}')
    print(f'Second part: {second_score}')