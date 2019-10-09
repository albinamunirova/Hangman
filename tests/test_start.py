"""This module tests the start of the game"""

from game import start
from mock import patch


def test_start():
    """This function tests the start of the game"""
    with patch('game.main') as perm_mock:
        perm_mock.return_value = True
        res = start.main()
    assert res
