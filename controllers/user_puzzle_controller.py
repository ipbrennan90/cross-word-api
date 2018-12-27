from controllers.puzzle_controller import PuzzleController
from database import db_session
from models import User


class UserPuzzleController():
    @classmethod
    def serialize(cls, puzzles):
        return [PuzzleController.serialize(p) for p in puzzles]

    @classmethod
    def show(cls, user_id):
        user = db_session.query(User).filter_by(id=user_id).one()
        return cls.serialize(user.puzzles)
