from services import SQLAlchemy


class DatabaseService:

    def __init__(self, type=None) -> None:
        self.type = type

    def create(self):
        if self.type == 'sqlalchemy':
            return SQLAlchemy()

        else:
            raise Exception('connection not created')
