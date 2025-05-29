"""
Created 2025
Simple number guessing game
Based on a web tutorial
Author: Piotr M
"""
import random
import re

NUMBER_LENGTH = 4


def play_again()->bool:
    """Function to ask user to play again"""
    while True:
        decision = input("Do you want to play again? (y/n): ")
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print("Please enter y or n.")


def is_correct_number(number:str)->bool:
    if(len(number) != NUMBER_LENGTH):
        return False

    x = re.search(r"\D", number)
    if(x != None):
        return False
    return True


def game_play():
    """This function manages one game"""
    #number generation
    number = random.randrange(10**(NUMBER_LENGTH-1), 10**NUMBER_LENGTH)
    number = str(number)

    guessed_digits = '_'
    turns = 1
    #print(number) #printing searched number for testing purposes

    next_round = True # for now, it remains unchanged, but quitting option might be added
    while next_round:
        n = input('Guess the {} digit number:'.format(NUMBER_LENGTH))

        if(is_correct_number(n)):
            guessed_digits = ''

            for i in range(NUMBER_LENGTH):
                if (n[i] == number[i]):
                    guessed_digits += number[i]
                else:
                    guessed_digits += '_'
        else:
            print('Please enter a correct number.')

        if(guessed_digits.find('_') == -1):
            print('Congratulations, you guessed the correct number in {} turn(s). '
                  'You are a Mastermind!'.format(turns))
            return
        else:
            print('You managed to guess the following: {}'.format(guessed_digits))
            turns += 1


def main():
    """Main function."""
    decision = True
    while decision:
        game_play()
        decision = play_again()


if __name__ == "__main__":
    main()