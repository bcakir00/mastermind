import algoritmes
import code
import io


number_of_rounds = None
number_of_pawns = None
number_of_colors = None


def check_if_game_ended():
    pass


def check_if_game_won():
    pass


def game(number_of_rounds):
    for round in range(number_of_rounds):
        print(round)





number_of_rounds = io.integer_input("Please input number of rounds: ")
number_of_pawns = input("Please input number of pawns (code length): ")
number_of_colors = input("Please input number of color (code depth): ")
game(number_of_rounds)