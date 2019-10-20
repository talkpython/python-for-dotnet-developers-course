from typing import List

import lib
import pytest_mock
# noinspection PyUnresolvedReferences
from test_fixtures import guitar_data


def test_something():
    assert 7 == 7


# def test_electric_guitars_wrong():
#     style = 'electric'
#     guitars = lib.all_guitars(style)
#     # sweet little generator expression
#     assert all(g.style == style for g in guitars)


def test_electric_guitars(guitar_data: List[lib.Guitar], mocker: pytest_mock.MockFixture):
    mocker.patch('lib.get_guitars_from_db', autospec=True, return_value=guitar_data)
    mocker.patch('lib.log', autospec=True)

    style = 'electric'
    guitars = lib.all_guitars(style)
    # sweet little generator expression
    assert all(g.style == style for g in guitars)


def test_all_guitars(guitar_data: List[lib.Guitar], mocker: pytest_mock.MockFixture):
    mocker.patch('lib.get_guitars_from_db', autospec=True, return_value=guitar_data)
    mocker.patch('lib.log', autospec=True)

    style = 'all'
    guitars = lib.all_guitars(style)
    # sweet little generator expression
    types = {g.style for g in guitars}

    assert types == {'acoustic', 'electric'}
