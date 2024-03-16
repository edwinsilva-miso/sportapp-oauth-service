from decouple import config
import pika


class AlertService:

    @classmethod
    def send_alert(cls, message):
        # Establishing queue connection
        rabbit_url = config('RABBITMQ_URL_CONNECTION')
        url_parameters = pika.URLParameters(rabbit_url)
        connection = pika.BlockingConnection(url_parameters)
        channel = connection.channel()
        channel.queue_declare(queue='alertas')

        # Send queue message
        channel.basic_publish(exchange='', routing_key='alertas', body=message)

        return 'Alert sent successfuly'
