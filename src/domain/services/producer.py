import pika


# Establish a connection
def produce_messages(queue_name, message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("rabbitmq-srv")
    )  # Replace with your RabbitMQ service name or IP

    # Create a channel
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=queue_name)

    # Publish a message
    msg = str(message)
    channel.basic_publish(exchange="", routing_key=queue_name, body=msg)
    print("published : ", msg)

    # Close the connection
    connection.close()
