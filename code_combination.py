import random


def generate_code():
    code = []

    for x in range(4):
        digit = random.randrange(1, 5)
        letter = chr(digit + 96)
        code.append(letter)

    return code


def scrub_combination_list(combination_list, feedback, code):
    combination_list.pop(0)

    for combination in combination_list:
        feedback_answer = list(feedback_computer(combination, code))

        if feedback_answer != feedback and feedback_answer != [4, 0]:

            combination_list.remove(combination)

    return combination_list


def generate_four_letter_code_combinations():
    #TODO: Make funtion abstract (parameter as input for size)
    combination_list = []

    for x in range(1, 5):
        first_letter = chr(x + 96)

        for y in range(1, 5):
            second_letter = chr(y + 96)

            for z in range(1, 5):
                third_letter = chr(z + 96)

                for q in range(1, 5):
                    fourth_letter = chr(q + 96)
                    combination_list.append([first_letter, second_letter, third_letter, fourth_letter])

    return combination_list


def max_partition_size_per_combination():
    all_code_combinations = generate_four_letter_code_combinations()
    worst_case_partition_dict = {}

    for guess in all_code_combinations:
        feedback_list = []
        feedback_count_dict = {'0,0': 0, '0,1': 0, '0,2': 0, '0,3': 0, '0,4': 0, '1,0': 0, '1,1': 0, '1,2': 0, '1,3': 0,
                               '2,0': 0, '2,1': 0, '2,2': 0, '3,0': 0, '3,1': 0, '4,0': 0}

        for combination in all_code_combinations:
            feedback = list(feedback_computer(guess, combination))
            feedback_list.append(feedback)

        for key in feedback_count_dict:
            lst_key = [int(key[0]), int(key[-1])]
            feedback_count_dict[key] = feedback_list.count(lst_key)

        max_partition_size = max(feedback_count_dict.values())
        worst_case_partition_dict[str(guess)] = max_partition_size

    return worst_case_partition_dict


def max_partition_size_per_combination2():
    all_code_combinations = generate_four_letter_code_combinations()
    worst_case_partition_dict = {}

    for guess in all_code_combinations:
        feedback_list = []
        feedback_count_dict = {'0,0': 0, '0,1': 0, '0,2': 0, '0,3': 0, '0,4': 0, '1,0': 0, '1,1': 0, '1,2': 0, '1,3': 0,
                               '2,0': 0, '2,1': 0, '2,2': 0, '3,0': 0, '3,1': 0, '4,0': 0}

        for combination in all_code_combinations:
            feedback = list(feedback_computer(guess, combination))
            feedback_list.append(feedback)

        for key in feedback_count_dict:
            lst_key = [int(key[0]), int(key[-1])]
            feedback_count_dict[key] = feedback_list.count(lst_key)

        max_partition_size = max(feedback_count_dict.values())
        worst_case_partition_dict[str(guess)] = max_partition_size

    return worst_case_partition_dict


def feedback_computer(guess, code):
    guess_letter_list = []
    guess_letter_non_duplicate_list = []
    code_letter_list = []
    correct_letters = 0
    correct_placements = 0

    for x in range(4):
        if guess[x] == code[x]:
            correct_placements += 1
        else:
            code_letter_list.append(code[x])
            guess_letter_list.append(guess[x])

            if guess[x] not in guess_letter_non_duplicate_list:
                guess_letter_non_duplicate_list.append(guess[x])

    for guess_letter in guess_letter_non_duplicate_list:
        count_guess = guess_letter_list.count(guess_letter)
        count_code = code_letter_list.count(guess_letter)

        correct_letters += min(count_guess, count_code)

    return correct_placements, correct_letters


def feedback_human(guess, code):
    print("The guess is " + str(guess) + " and the code was " + str(code))

    correct_placements = int(input("How many placements and colors are correct: ")) #TODO: validate user input
    correct_colors = int(input("How many only colors are correct: ")) #TODO: validate user input

    return [correct_placements, correct_colors]