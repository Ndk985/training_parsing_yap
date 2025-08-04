# work_with_db.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declared_attr, declarative_base
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete


# Обычно класс, на основе которого создаётся декларативная база,
# называют так же, как и сам класс декларативной базы.
class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        # При представлении объекта класса Pep 
        # будут выводиться значения полей pep_number и name.
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    session = Session(engine)

    session.execute(
    delete(Pep).where(Pep.status == 'Active')
    )
    session.commit()