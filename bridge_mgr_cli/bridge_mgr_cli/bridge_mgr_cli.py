import argparse
import requests
import ConfigParser
import pika

def create_bridge(bridge_name):
    url = get_rest_server_url('create_bridge')

    response = requests.post(url, data={'bridge_name':bridge_name})

    print response.text

def remove_bridge(bridge_name):
    url = get_rest_server_url('remove_bridge')

    response = requests.post(url, data={'bridge_name':bridge_name})

    print response.text

def get_bridges():
    url = get_rest_server_url('get_bridges')

    response = requests.post(url)

    print response.text

def get_rest_server_url(request_name):
    config = ConfigParser.RawConfigParser()

    config.read('config.cfg')

    section_name = 'rest_server'

    host = config.get(section_name, 'host')
    port = config.get(section_name, 'port')

    request = 'http://{0}:{1}/{2}'.format(host, port, request_name)

    return request

def parse_cmd_line():
    parser = argparse.ArgumentParser(description='process command line')

    parser.add_argument('--cb', dest='create_bridge', type=str, help='create bridge <name>')
    parser.add_argument('--rb', dest='remove_bridge', type=str, help='remove bridge <name>')
    parser.add_argument('--gb', dest='get_bridges', action='store_true', help='get bridges')

    args = parser.parse_args()

    if args.create_bridge:
        create_bridge(args.create_bridge)
    elif args.remove_bridge:
        remove_bridge(args.remove_bridge)
    elif args.get_bridges:
        get_bridges()

def test_rabbitmq():
    credentials = pika.PlainCredentials('guest', 'guest')

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    connection.close()

def rabbitmq_read():
    credentials = pika.PlainCredentials('guest', 'guest')

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    k = 4

if __name__ == '__main__':
    #parse_cmd_line()
    #rabbitmq_send()
    rabbitmq_read()