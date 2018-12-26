from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base, db_session
import pdb


class Puzzle(Base):
    __tablename__ = 'puzzles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    board = relationship("Board", uselist=False, back_populates="puzzle")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Puzzle %r>' % (self.name)
