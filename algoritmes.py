# loop
    # let algorithem guess code
    # ask user for feedback
    # check if game won or ended, if not loop one more time


import code_combination


def a_simple_strategy(code):
    all_code_combinations = code_combination.generate_four_letter_code_combinations()
    popped_code_combinations = []

    for round in range(11):
        feedback_answer = code_combination.feedback_human(all_code_combinations[0], code)

        if round == 0:
            popped_code_combinations = all_code_combinations

        if feedback_answer == [4, 0]:
            print("The code has been cracked.")
            exit()
        elif round == 11:
            print("The code has not been broken. The code was " + str(code))
            exit()
        else:
            popped_code_combinations = code_combination.scrub_combination_list(popped_code_combinations,
                                                                               feedback_answer, code)


def worst_case_strategy(code):
    pass


def a_new_strategy(code):
    pass


def heuristic_strategy(code):
    #make four guesses with duplicates (e.g. aaaa, bbbb, etc.) and safe per letter how many there are.
    #swap pairs randomly, but check if the the letters are not the same and if the result of the swap hasn't been guessed before
    swap_counter = 0
    guess = []
    letter_amount_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0
    }

    for x in range(11):
        if x <= 2:
            letter = chr(x + 97)
            letter_amount_dict[letter] = code_combination.feedback_human([letter, letter, letter, letter], code)[0]
            letter_amount_dict["d"] = 4 - letter_amount_dict["a"] - letter_amount_dict["b"] - letter_amount_dict["c"]

            #TODO: Put in function and add in code_combination module
            if x == 2:
                keys = letter_amount_dict.keys()

                for key in keys:
                    letter = key
                    amount = letter_amount_dict.get(key)

                    for x in range(amount):
                        guess.append(letter)
        else:
            if code_combination.feedback_human(guess, code) == [4, 0]:
                print("The code has been cracked.")
                exit()
            elif x == 7:
                print("The code has not been broken. The code was " + str(code))
            else:
                # swap pair
                if x % 3 == 0:
                    #swap first pair
                    pass
                if x % 3 == 1:
                    #swap middle pair
                    pass
                if x % 3 == 2:
                    #swap last pair
                    pass