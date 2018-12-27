from database import db_session
from models import User
from database import db_session
from controllers.puzzle_controller import PuzzleController


class UserController():
    @classmethod
    def serialize(cls, user):
        return {
            'id': user.id,
            'email': user.email,
            'puzzles': [PuzzleController.serialize(p) for p in user.puzzles]
        }

    @classmethod
    def index(cls):
        users = db_session.query(User).all()
        users_response = [cls.serialize(user) for user in users]
        return users_response

    @classmethod
    def show(cls, user_id):
        user = db_session.query(User).filter_by(id=user_id).one()
        return cls.serialize(user)
