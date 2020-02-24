from .base import Base
from sqlalchemy import Integer, String, Column

class Book(Base):
    __tablename__ = 'books'
    name = Column(String, primary_key=True)
    year = Column(Integer)