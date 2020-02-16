#ask user who should be the codebreaker

#if codebreaker is human
    #generate code
    #loop n times
        #ask guess
        #give feedback
    #check if game won or ended, if not loop one more time

#if codebreaker is computer
    #ask code
    #ask game mode (algorithem)
    #let algorithem guess code
    #ask user for feedback
    #check if game won or ended, if not loop one more time


import algoritmes
import code_combination


def check_if_game_ended(round):
    if round == 10:
        return True
    else:
        return False


def check_if_game_won(guess, code):
    if guess == code:
        return True
    else:
        return False


def feedback(guess, code):
    guess_non_duplicates = list(dict.fromkeys(guess))
    correct_letters = 0
    correct_placements = 0

    for x in range(4):
        a = guess[x]
        b = code[x]

        if guess[x] == code[x]:
            correct_placements += 1

    for letter in guess_non_duplicates:
        correct_letters += code.count(letter)

    return (correct_placements, abs(correct_letters - correct_placements))


print("Codebreaker: \n"
      "1 - Computer \n"
      "2 - Human \n")
codebreaker = input("Please select codebreaker: ") #TODO: validate input

if codebreaker == "2":
    code = code_combination.generate_code()

    for round in range(11):
        guess = list(input("Please insert guess in letters, from a to d (e.g. abcd): ")) #TODO: validate input

        feedback_answer = feedback(guess, code)
        print(feedback_answer)

        if check_if_game_won(guess, code):
            print("The code has been broken.")
            exit()
        elif check_if_game_ended(round):
            print("The code has not been cracked.")
else:
    code = list(input("Please insert code in letters, from a to d (e.g. abcd): "))  # TODO: validate input

    print("Game modes: \n"
         "1 - Worst Case Strategy \n"
        "2 - A New Strategy \n"
        "3 - Heuristic Strategy \n")
    game_mode = input("Please select game mode: ")

