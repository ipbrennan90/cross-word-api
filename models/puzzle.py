from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base, db_session


class Puzzle(Base):
    __tablename__ = 'puzzles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    board = relationship("Board", uselist=False, back_populates="puzzle")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def serialize(cls, puzzle):
        return {
            'id': puzzle.id,
            'name': puzzle.name,
            'created_at': puzzle.created_at,
            'updated_at': puzzle.updated_at,
            'board': {
                'rows': [row.columns for row in puzzle.board.rows]
            }
        }

    @classmethod
    def findAll(cls):
        puzzles = db_session.query(Puzzle).all()
        puzzles_response = [cls.serialize(puzzle) for puzzle in puzzles]
        return puzzles_response

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Puzzle %r>' % (self.name)
