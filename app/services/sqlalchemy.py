from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import select, insert, update, column, text
from orm import PatientsTable
from configuration import DATABASE_URL

engine = create_engine(
    DATABASE_URL
)

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)


class PatientsService:

    def __init__(self) -> None:
        pass

    def get_patients_list(self, session: scoped_session):
        session.begin()
        result = session.scalars(select(PatientsTable)).all()
        return result


class SQLAlchemy(
    PatientsService
):

    _session = session

    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQLAlchemy, cls).__new__(cls)
        return cls.instance

    def connection(self):
        return self._session

    def get_patients_list(self):
        return super().get_patients_list(session=self._session)
