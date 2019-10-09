import sys
import io
from game import Game


def test_print_word():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    new_game = Game()
    new_game.hidden_word = 'love'
    guessed_letters = {'l', 'e'}
    new_game.print_word(guessed_letters)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'The word: l**e\n'
