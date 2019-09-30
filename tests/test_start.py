from hangman import start
from mock import patch


def test_start():

    with patch('game.main') as perm_mock:
        perm_mock.return_value = True
        res = start.main()
    assert res