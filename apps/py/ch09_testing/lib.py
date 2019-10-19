from typing import List, Optional
from colorama import Fore


class Guitar:
    def __init__(self, name: str = None, price: float = 0.0,
                 img: str = None, style: str = None):
        self.style = style
        self.img = img
        self.price = price
        self.name = name


def all_guitars(style: Optional[str]) -> List[Guitar]:
    if not style or not style.strip():
        raise ValueError("'style' cannot be empty.")

    style = style.lower()

    log(f"Guitars for {style}")
    guitars = get_guitars_from_db()
    if style == 'all':
        return guitars

    return [
        g
        for g in guitars
        if g.style == style
    ]


def log(msg: str):
    # raise Exception("NO LOG!")
    print(Fore.YELLOW + "LOGGING THIS TO A FILE, SHOULD NOT SEE IN TEST: " + Fore.WHITE + f"{msg}.")


# noinspection DuplicatedCode
def get_guitars_from_db():
    # raise Exception("NO DB!")
    print(Fore.YELLOW + "GETTING GUITARS FROM DB! Should not see in test." + Fore.WHITE)
    # This guitar data simulates what we would actually get back from the database.
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
    return guitars
