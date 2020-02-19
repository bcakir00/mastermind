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
    #loop
        #let algorithem guess code
        #ask user for feedback
        #check if game won or ended, if not loop one more time


import algoritmes
import code_combination


print("Codebreaker: \n"
      "1 - Computer \n"
      "2 - Human \n")
codebreaker = input("Please select codebreaker: ")

if codebreaker == "2":
    code = code_combination.generate_code()

    for round in range(11):
        guess = list(input("Please insert guess in letters, from a to d (e.g. abcd): ")) #TODO: validate input

        feedback_answer = code_combination.feedback_computer(guess, code)
        print(feedback_answer)

        if guess == code:
            print("The code has been cracked.")
            exit()
        elif round == 10:
            print("The code has not been broken. The code was " + str(code))
elif codebreaker == "1":
    print("Game modes: \n"
        "1 - A Simple Strategy \n"
        "2 - Worst Case Strategy \n"
        "3 - Heuristic Strategy \n")
    game_mode = int(input("Please select game mode: "))

    code = list(input("\nPlease insert code in letters, from a to d (e.g. abcd): ")) #TODO: validate input

    if game_mode == 1:
        algoritmes.a_simple_strategy(code)
    elif game_mode == 2:
        algoritmes.worst_case_strategy(code)
    else:
        algoritmes.heuristic_strategy(code)