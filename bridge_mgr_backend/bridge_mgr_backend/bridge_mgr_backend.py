import pika
import ConfigParser

def listen_rabbitmq():
    config = ConfigParser.RawConfigParser()

    config.read('config.cfg')

    section_name = 'rabbitmq_server'

    host = config.get(section_name, 'host')
    port = config.get(section_name, 'port')
    user_name = config.get(section_name, 'user_name')
    password = config.get(section_name, 'password')
    request_queue_name = config.get(section_name, 'request_queue_name')
    response_queue_name = config.get(section_name, 'response_queue_name')

    credentials = pika.PlainCredentials(user_name, password)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))

    channel = connection.channel()

    channel.queue_declare(queue=request_queue_name)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue=request_queue_name,
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    listen_rabbitmq()