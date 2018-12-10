from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True)
    puzzle_id = Column(Integer, ForeignKey('puzzles.id'))
    puzzle = relationship("Puzzle", back_populates="board")
    rows = relationship("Row", back_populates="board")

    def __init__(self, puzzle):
        self.puzzle = puzzle
