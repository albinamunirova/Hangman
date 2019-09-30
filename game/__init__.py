import random


def print_word(word, letters):
    line = ''
    for i in word:
        if i in letters:
            line += i
        else:
            line += '*'
    print('The word:', line, '\n')


def check(word, letters):
    answer = True
    for i in word:
        if i not in letters:
            answer = False
    return answer


class Game(object):

    def __init__(self):

        self.dictionary = ['hello', 'bird', 'car', 'table']
        self.word = []
        self.letters = set()

        self.play_flg = True

        self.mistakes = 5
        self.missed = 0

    def iteration(self):

        letter = input()
        self.letters.add(letter)

        if letter in self.word:

            print('Hit!\n')

            if check(self.word, self.letters):
                print_word(self.word, self.letters)
                print('You won!')
                self.play_flg = False
        else:

            self.missed += 1
            print('Missed, mistake', self.missed, 'out of', self.mistakes, '\n')

            if self.missed >= self.mistakes:
                print_word(self.word, self.letters)
                print('You lost!')
                self.play_flg = False

    def play(self):

        self.word = random.choice(self.dictionary)

        while self.play_flg:
            print_word(self.word, self.letters)
            print('Guess a letter:')
            self.iteration()


def main():
    new_game = Game()
    new_game.play()
    return True