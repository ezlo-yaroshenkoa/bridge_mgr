import pika

class BridgeManagerRpcServer(object):
    def __init__(self, host, port, user_name, password, queue_name):
        credentials = pika.PlainCredentials(user_name, password)

        self.connection_ = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials))

        self.channel_ = self.connection_.channel()

        self.channel_.queue_declare(queue=queue_name)

        def on_request(channel, method, props, body):
            # to do parse body
            # to do do work
            # to do send response

            response = 'ready';

            channel.basic_publish(exchange='',
                                  routing_key=props.reply_to,
                                  properties=pika.BasicProperties(correlation_id=props.correlation_id),
                                  body=response)

            channel.basic_ack(delivery_tag=method.delivery_tag)

        self.channel_.basic_qos(prefetch_count=1)
        self.channel_.basic_consume(on_request, queue=queue_name)

    def start(self):
        self.channel_.start_consuming()

if __name__ == '__main__':
    #to do read config

    server = BridgeManagerRpcServer();

    server.start();