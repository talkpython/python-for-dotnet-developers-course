from guitary.data.guitar import Guitar
from guitary.data import session_factory


def load_guitars_if_empty():
    with session_factory.create_session() as ctx:
        count = ctx.session.query(Guitar).count()
        if count > 0:
            print(f'Not adding new data, there are {count} guitars already.')
            return

        guitars = [
            Guitar(name='AX Black', price=499, img='/static/img/guitars/ax-black.jpg', style='electric'),
            Guitar(
                name='Jet Black Electric', price=599, img='/static/img/guitars/jet-black-electric.jpg', style='electric'
            ),
            Guitar(name='Weezer Classic', price=1499, img='/static/img/guitars/weezer-classic.jpg', style='electric'),
            Guitar(name='Acoustic Black', price=1298, img='/static/img/guitars/black-acoustic.jpg', style='acoustic'),
            Guitar(name='Mellow Yellow', price=799, img='/static/img/guitars/mellow-yellow.jpg', style='electric'),
            Guitar(name='White Vibes', price=699, img='/static/img/guitars/white-vibes.jpg', style='electric'),
            Guitar(
                name='Brush Riffs', price=599, img='/static/img/guitars/brushed-black-electric.jpg', style='electric'
            ),
            Guitar(name="Nature's Song", price=799, img='/static/img/guitars/natures-song.jpg', style='electric'),
            Guitar(
                name='Electric Wood Grain',
                price=399,
                img='/static/img/guitars/woodgrain-electric.jpg',
                style='electric',
            ),
        ]

        # Do work here...
        for guitar in guitars:
            ctx.session.add(guitar)

        ctx.session.commit()
