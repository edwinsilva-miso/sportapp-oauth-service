from flask import Blueprint, request, jsonify
import datetime

from src.services.AuthenticationService import AuthenticationService
from src.services.AlertService import AlertService

main = Blueprint('alerts_blueprint', __name__)


@main.route('/', methods=['POST'])
def generate_alert():
    has_access = AuthenticationService.verify_token(request.headers)

    if has_access:
        ''' 
        Implement here the generate alert logic
        It's suggested create a new service in order to perform this action  
        '''
        mensaje = request.json['mensaje']
        hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtener la hora actual
        critico = request.json.get('critico', False)
        
        # Crear el mensaje con la hora
        mensaje = f"{hora}: {mensaje}: {critico}"
        response = AlertService.enviar_alerta(mensaje)
        return {'status': response}
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401

