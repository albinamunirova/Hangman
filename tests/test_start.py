"""This module tests the start of the game"""

from mock import patch
from game import start


def test_start():
    """This function tests the start of the game"""
    with patch('game.main') as perm_mock:
        perm_mock.return_value = True
        res = start.main()
    assert res
