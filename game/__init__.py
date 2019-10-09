import random


class Game():
"""
Main game class realization
"""
    def __init__(self):
        self._max_mistakes = 5
        self._flag_guessed = False
        self._words = ['love', 'program', 'architecture']

    def play(self):

        hidden_word = random.choice(self._words)

        mistakes = 0
        guessed_letters = set()
        needed_letters = set(hidden_word)

        while mistakes < self._max_mistakes and not self._flag_guessed:
            print("Guess a letter:")
            cur_letter = input()
            if cur_letter in needed_letters:
                guessed_letters.add(cur_letter)
                print("Hit!")
                if guessed_letters == needed_letters:
                    self._flag_guessed = True
            else:
                mistakes += 1
                max_m = self._max_mistakes
                print("Missed, mistake {} out of {}.".format(mistakes, max_m))

            print("The word: ", end="")
            for i in hidden_word:
                if i in guessed_letters:
                    print(i, end="")
                else:
                    print("*", end="")
            print()
        if self._flag_guessed:
            print("You won!")
        else:
            print("You lost!")


def main():
    new_game = Game()
    new_game.play()
    return True
