from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base


class Row(Base):
    __tablename__ = 'rows'
    id = Column(Integer, primary_key=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    board = relationship("Board", back_populates="rows")
    columns = Column(ARRAY(String))

    def __init__(self, board, columns=[]):
        self.columns = columns
        self.board = board
