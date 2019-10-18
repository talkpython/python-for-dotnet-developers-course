from sqlalchemy.orm import Session


class ContextSession:
    def __init__(self, session: Session):
        self.session: Session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            try:
                self.session.rollback()
            except:
                pass

        self.session.close()
