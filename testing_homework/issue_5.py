from unittest.mock import patch
from what_is_year_now import what_is_year_now


def test_yymmdd():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '2023-11-05'}
        assert what_is_year_now() == 2023
        mocked.assert_called_once()


def test_ddmmyy():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '05.11.2023'}
        assert what_is_year_now() == 2023
        mocked.assert_called_once()


def test_type_exception():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {1}
        error = False
        try:
            what_is_year_now()
        except TypeError:
            error = True
        finally:
            assert error
        mocked.assert_called_once()


def test_value_exception():
    with patch('what_is_year_now.json.load') as mocked:
        mocked.return_value = {'currentDateTime': '00000000'}
        error = False
        try:
            what_is_year_now()
        except ValueError:
            error = True
        finally:
            assert error
        mocked.assert_called_once()
