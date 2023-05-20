import ssl
import pika

def create_pika_connection(rabbitmq_broker_id, rabbitmq_user, rabbitmq_password, region):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

    url = f"amqps://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_broker_id}.mq.{region}.amazonaws.com:5671"
    parameters = pika.URLParameters(url)
    parameters.ssl_options = pika.SSLOptions(context=ssl_context)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection, channel

def close_connection(connection):
    connection.close()
