from flask import Blueprint, request, jsonify

from src.services.AuthenticationService import AuthenticationService

main = Blueprint('alerts_blueprint', __name__)


@main.route('/', methods=['POST'])
def generate_alert():
    has_access = AuthenticationService.verify_token(request.headers)

    if has_access:
        ''' 
        Implement here the generate alert logic
        It's suggested create a new service in order to perform this action  
        '''
        print('Echo')
        return {'alert': request.json["alert"]}
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

