from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)

    def __init__(self, email=None):
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.email)
