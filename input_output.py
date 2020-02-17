def range_validation(data, min, max):
    if len(data) > min and len(data) < max:
        return True
    else:
        return False


def type_validation(actual_type, desired_type):
    if actual_type == desired_type:
        return True
    else:
        return False


def max_length_validation(length, max):
    if length < max:
        return True
    else:
        return False


def feedback_computer(guess, code):
    guess_non_duplicates = list(dict.fromkeys(guess))
    correct_letters = 0
    correct_placements = 0

    for x in range(4):
        if guess[x] == code[x]:
            correct_placements += 1

    for letter in guess_non_duplicates:
        correct_letters += code.count(letter)

    return (correct_placements, abs(correct_letters - correct_placements))


def feedback_human(guess, code):
    print("The guess is " + str(guess) + " and the code was " + str(code))

    correct_placements = int(input("How many placements and colors are correct: ")) #TODO: validate user input
    correct_colors = int(input("How many only colors are correct: ")) #TODO: validate user input

    return [correct_placements, correct_colors]