import pika


class AlertService:

    @classmethod
    def enviar_alerta(cls, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='alertas')
        
        channel.basic_publish(exchange='', routing_key='alertas', body=message)
        return 'Mensaje enviado correctamente'

