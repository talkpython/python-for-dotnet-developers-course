from typing import List, Optional

from guitary.data.guitar import Guitar


def all_guitars(style: Optional[str]) -> List[Guitar]:
    guitars = [
        Guitar('AX Black', 499, '/static/img/guitars/ax-black.jpg', style='electric'),
        Guitar('Jet Black Electric', 599, '/static/img/guitars/jet-black-electric.jpg', style='electric'),
        Guitar('Weezer Classic', 1499, '/static/img/guitars/weezer-classic.jpg', style='electric'),
        Guitar('Acoustic Black', 1299, '/static/img/guitars/black-acoustic.jpg', style='acoustic'),
        Guitar('Mellow Yellow', 799, '/static/img/guitars/mellow-yellow.jpg', style='electric'),
        Guitar('White Vibes', 699, '/static/img/guitars/white-vibes.jpg', style='electric'),
        Guitar('Brush Riffs', 599, '/static/img/guitars/brushed-black-electric.jpg', style='electric'),
        Guitar("Nature's Song", 799, '/static/img/guitars/natures-song.jpg', style='electric'),
        Guitar('Electric Wood Grain', 399, '/static/img/guitars/woodgrain-electric.jpg', style='electric'),
    ]
    guitars.sort(key=lambda g: g.price, reverse=True)

    if style is None or style == 'all':
        return guitars

    filtered_guitars = [
        g
        for g in guitars
        if g.style == style
    ]

    return filtered_guitars
