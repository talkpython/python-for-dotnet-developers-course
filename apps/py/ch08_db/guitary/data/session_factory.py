from typing import Optional, Callable

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.orm import Session, scoped_session

from guitary.data.context_session import ContextSession
from guitary.db import db_folder

__engine = None
__factory: Optional[Callable[[], Session]] = None


def global_init(db_name: str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = scoped_session(sqlalchemy.orm.sessionmaker(bind=__engine))


def create_tables():
    if not __engine:
        raise Exception('You must call global_init() first.')

    # noinspection PyUnresolvedReferences
    from guitary.data.guitar import Guitar
    from guitary.data.sqlalchemybase import SqlAlchemyBase

    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> ContextSession:
    if not __factory:
        raise Exception('You must call global_init() first.')

    session = __factory()
    session.expire_on_commit = False

    return ContextSession(session)
