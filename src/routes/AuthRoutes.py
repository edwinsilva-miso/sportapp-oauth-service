from flask import Blueprint, request, jsonify

from src.services.AuthenticationService import AuthenticationService


main = Blueprint('auth_blueprint', __name__)


@main.route('/', methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json['password']

    encoded_token = AuthenticationService.login_user(username, password)

    if encoded_token is not None:
        return jsonify({'success': True, 'token': encoded_token})
    else:
        response = jsonify({'message': 'Invalid credentials'})
        return response, 401
