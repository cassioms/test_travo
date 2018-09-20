import sqlite3
from http import HTTPStatus
from flask import Flask, request, jsonify

from aula03.user_service import UserService
from aula03.user import User

app = Flask(__name__)

user_service = UserService('app.db')

@app.route("/users")
def hello():
    return jsonify({'users': user_service.list_users()})


@app.route('/users/add', methods=['POST'])
def new_user():
    user_json = request.json
    user_service.add_user(user_json['id'], user_json['name'], user_json['height'], user_json['weight'])
    return jsonify(user_json), HTTPStatus.CREATED


@app.route('/users/update/<_id>', methods=['PUT'])
def update_user(_id):
    user_json = request.json
    user_service.update_user(_id, user_json['name'], user_json['height'], user_json['weight'])
    return jsonify(user_json)


@app.route('/users/delete/<_id>', methods=['DELETE'])
def delete_user(_id):
    user_service.delete_user(_id)
    return '', HTTPStatus.NO_CONTENT
