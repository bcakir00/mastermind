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


def feedback_computer(guess, code):
    guess_letter_list = []
    code_letter_list = []
    correct_letters = 0
    correct_placements = 0

    for x in range(4):
        if guess[x] == code[x]:
            correct_placements += 1
        else:
            code_letter_list.append(code[x])
            guess_letter_list.append(guess[x])

    for guess_letter in guess_letter_list:
        if guess_letter in code_letter_list:
            correct_letters += 1

    return correct_placements, correct_letters


def feedback_human(guess, code):
    print("The guess is " + str(guess) + " and the code was " + str(code))

    correct_placements = int(input("How many placements and colors are correct: ")) #TODO: validate user input
    correct_colors = int(input("How many only colors are correct: ")) #TODO: validate user input

    return [correct_placements, correct_colors]