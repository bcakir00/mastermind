# loop
    # let algorithem guess code
    # ask user for feedback
    # check if game won or ended, if not loop one more time


import code_combination
import input_output


def a_simple_strategy(code):
    all_code_combinations = code_combination.generate_four_letter_code_combinations()

    for round in range(11):
        feedback_answer = input_output.feedback_human(all_code_combinations[0], code)

        if feedback_answer == code:
            print("The code has been cracked.")
        elif round == 11:
            print("The code has not been broken. The code was " + str(code))
        else:
            pass
            #scrub list


def worst_case_strategy(code):
    pass


def a_new_strategy(code):
    pass


def heuristic_strategy(code):
    #make four guesses with duplicates (e.g. aaaa, bbbb, etc.) and safe per letter how many there are.


    pass