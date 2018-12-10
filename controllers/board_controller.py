from database import db_session
from models import Row
from models import Board
from models import Puzzle
from database import db_session


class BoardController():
    board = None

    def __init__(self, request_type, params):
        if request_type == 'POST':
            self.board = self.create(**params)

    def create(self, puzzle_id, board_rows):
        puzzle = db_session.query(Puzzle).filter(Puzzle.id == puzzle_id).one()
        board = Board(puzzle=puzzle)
        db_session.add(board)
        for row in board_rows:
            board_row = Row(board=board, columns=row)
            db_session.add(board_row)
        db_session.commit()
        return board
