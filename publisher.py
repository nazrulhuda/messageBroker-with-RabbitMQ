import json
from basicClient import create_pika_connection, close_connection

def send_message(connection, channel, exchange, routing_key, body):
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
    print(f"Sent message. Exchange: {exchange}, Routing Key: {routing_key}, Body: {body}")

if __name__ == "__main__":
    rabbitmq_broker_id = "b-cb5e342c-c7e4-4a62-93aa-9192e138e2f4"
    rabbitmq_user = "nafiz"
    rabbitmq_password = "kie5gierai0Uyoh1Ai$j"
    region = "us-east-1"
    queue_name = "a"
    exchange = ""
    routing_key = queue_name
    json_body={"Hello World":"fs"}
    message_body =json.dumps(json_body)

    connection, channel = create_pika_connection(rabbitmq_broker_id, rabbitmq_user, rabbitmq_password, region)

    send_message(connection, channel, exchange, routing_key, message_body)
    print("dsfd")

    close_connection(connection)