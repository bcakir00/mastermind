import random


def generate_code():
    code = []

    for x in range(4):
        digit = random.randrange(1, 5)
        letter = chr(digit + 96)
        code.append(letter)

    return code


def scub_combination_list(combination_list):
    pass


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