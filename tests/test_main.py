"""This module tests the main function"""
from mock import patch
from game import main, Game


def test_main():
    """This function tests the main function"""
    def new_play(self):
        """We need this function to test the main function"""
        self.boolean = False

    with patch.object(Game, 'play', new_play):
        result = main()
    assert result
