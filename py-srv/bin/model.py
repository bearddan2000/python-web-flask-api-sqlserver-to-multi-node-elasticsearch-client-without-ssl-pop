from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DbModel(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    breed = Column(String(20))
    color = Column(String(10))

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def __repr__(self):
        return "<%s('%s', '%s')>" % (self.__tablename__, self.breed, self.color)
