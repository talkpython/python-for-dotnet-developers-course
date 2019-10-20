from typing import List
import pytest
import lib


@pytest.fixture
def guitar_data() -> List[lib.Guitar]:
    # This guitar data simulates our mock data to avoid DB calls and dependencies.
    guitars = [
        lib.Guitar('Jet Black Electric', 599, '/static/img/guitars/jet-black-electric.jpg', style='electric'),
        lib.Guitar('Weezer Classic', 1499, '/static/img/guitars/weezer-classic.jpg', style='electric'),
        lib.Guitar('Acoustic Black', 1299, '/static/img/guitars/black-acoustic.jpg', style='acoustic'),
        lib.Guitar('Brush Riffs', 599, '/static/img/guitars/brushed-black-electric.jpg', style='electric'),
        lib.Guitar('Electric Wood Grain', 399, '/static/img/guitars/woodgrain-electric.jpg', style='electric'),
    ]
    guitars.sort(key=lambda g: g.price, reverse=True)
    return guitars
