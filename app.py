from flask import Flask, request
from database import db_session
from controllers import BoardController, PuzzleController, UserController, UserPuzzleController
from routes import Router
from models import Puzzle
from flask_json import FlaskJSON, json_response
from flask_cors import CORS
import json
import pdb

app = Flask(__name__)
FlaskJSON(app)
CORS(app)

# @app.route('/puzzle', methods=['POST'])
# def puzzle():
#     if request_method == 'POST':


@app.route('/board', methods=['POST'])
def board():
    new_board = BoardController(
        request.method, json.loads(request.data) or None)
    new_board_rows = [row.columns for row in new_board.board.rows]
    response = {
        'puzzle_id': new_board.board.puzzle_id,
        'rows': new_board_rows
    }
    return json_response(**response)


@app.route('/puzzles', methods=['GET'])
@app.route('/puzzles/<int:puzzle_id>', methods=['GET'])
def puzzles(**params):
    data = Router.direct(PuzzleController, request.method, params)
    return json_response(data=data)


@app.route('/users', methods=['GET'])
@app.route('/users/<int:user_id>', methods=['GET'])
def users(**params):
    data = Router.direct(UserController, request.method, params)
    return json_response(data=data)


@app.route('/users/<int:user_id>/puzzles', methods=['GET'])
def user_puzzles(**params):
    data = Router.direct(UserPuzzleController, request.method, params)
    return json_response(data=data)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
