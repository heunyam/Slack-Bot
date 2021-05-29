from app.models import Base, session
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = 'user'
    id = Column(String(40), primary_key=True)
    password = Column(String(40))
    name = Column(String(40))

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name

    def save(self):
        session.add(self)
        session.commit()
        return self
