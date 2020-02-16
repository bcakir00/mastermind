import random


def generate_code():
    code = []

    for x in range(4):
        digit = random.randrange(1, 5)
        letter = chr(digit + 96)
        code.append(letter)

    return code


def guess_code():
    pass


def generate_all_code_combinations():
    pass