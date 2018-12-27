from database import db_session
from models import Puzzle


class PuzzleController():

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
    def index(cls):
        puzzles = db_session.query(Puzzle).all()
        puzzles_response = [cls.serialize(puzzle) for puzzle in puzzles]
        return puzzles_response

    @classmethod
    def show(cls, puzzle_id):
        puzzle = db_session.query(Puzzle).filter_by(id=puzzle_id).one()
        return cls.serialize(puzzle)
