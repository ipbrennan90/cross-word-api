from flask import Flask, request
from database import db_session
from controllers import BoardController
from models import Puzzle
from flask_json import FlaskJSON, json_response
from flask_cors import CORS
import json

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
def puzzles():
    puzzles = Puzzle.findAll()
    return json_response(data=puzzles)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
