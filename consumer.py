import json
from basicClient import create_pika_connection, close_connection

def consume_messages(connection, channel, queue):
    def callback(ch, method, properties, body):
        message = body

        print(message)

        

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



if __name__ == "__main__":
    rabbitmq_broker_id = ""
    rabbitmq_user = ""
    rabbitmq_password = ""
    region = ""
    queue_name = "a"

    connection, channel = create_pika_connection(rabbitmq_broker_id, rabbitmq_user, rabbitmq_password, region)

    consume_messages(connection, channel, queue_name)

    close_connection(connection)