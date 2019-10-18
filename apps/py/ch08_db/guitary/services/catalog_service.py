from typing import List, Optional

from guitary.data.guitar import Guitar
from guitary.data import session_factory


def all_guitars(style: Optional[str]) -> List[Guitar]:
    with session_factory.create_session() as ctx:
        if style is None or style == 'all':
            guitars = ctx.session.query(Guitar).order_by(Guitar.price.desc())
            return list(guitars)

    filtered_guitars = list(ctx.session.query(Guitar)
                            .filter(Guitar.style == style)
                            .order_by(Guitar.price.desc()))

    return filtered_guitars
