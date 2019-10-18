import sqlalchemy as sa
from guitary.data.sqlalchemybase import SqlAlchemyBase


class Guitar(SqlAlchemyBase):
    __tablename__ = 'guitars'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String)
    style: str = sa.Column(sa.String, index=True)
    img: str = sa.Column(sa.String)
    price: float = sa.Column(sa.Float, index=True)
