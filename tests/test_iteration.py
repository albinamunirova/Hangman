import sys
import io
from game import Game
from mock import patch


def test_iteration():

    # test_1
    captured_output = io.StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()

    with patch('hangman.letter_input') as perm_mock:

        perm_mock.return_value = 'r'
        new_game.word = 'car'
        new_game.missed = 3
        new_game.letters = {'c','a'}
        new_game.iteration()

    sys.stdout = sys.__stdout__

    assert captured_output.getvalue() == 'Hit!\n\nThe word: car\n\nYou won!\n'
    assert new_game.missed == 3
    assert new_game.letters == {'c', 'a'}

    # test_2
    captured_output = io.StringIO.StringIO()
    sys.stdout = captured_output
    new_game = Game()

    with patch('hangman.letter_input') as perm_mock:

        perm_mock.return_value = 'e'
        new_game.word = 'bird'
        new_game.missed = 4
        new_game.letters = {'b','i','r'}
        new_game.iteration()

    sys.stdout = sys.__stdout__

    printed_str = 'Missed, mistake 5 out of 5 \n\nThe word: ***\n\nYou lost!\n'

    assert captured_output.getvalue() == printed_str
    assert new_game.missed == 5
    assert new_game.letters == {'k', 'e'}