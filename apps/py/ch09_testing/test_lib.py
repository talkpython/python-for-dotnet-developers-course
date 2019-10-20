import lib
from test_fixtures import guitar_data


def test_something():
    assert 7 == 7


# def test_electric_guitars_wrong():
#     style = 'electric'
#     guitars = lib.all_guitars(style)
#     # sweet little generator expression
#     assert all(g.style == style for g in guitars)


def test_electric_guitars(guitar_data):
    style = 'electric'
    guitars = lib.all_guitars(style)
    # sweet little generator expression
    assert all(g.style == style for g in guitars)
