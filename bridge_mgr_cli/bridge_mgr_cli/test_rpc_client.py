import pika
import uuid

class BridgeManagerRpcClient(object):
    def __init__(self, host, port, user_name, password, queue_name):
        credentials = pika.PlainCredentials(user_name, password)

        self.queue_name_ = queue_name

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host, port=port, credentials=credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.request_id_ == props.correlation_id:
            self.response = body

    def send_data(self, action_data):
        self.response = None
        self.request_id_ = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name_,
                                   properties=pika.BasicProperties(
                                           reply_to=self.callback_queue,
                                           correlation_id=self.request_id_,
                                   ),
                                   body=action_data)

        while self.response is None:
            self.connection.process_data_events()

        return self.response


bridge_mgr_rpc_client = BridgeManagerRpcClient('localhost', 5672, 'guest', 'guest', 'rpc_queue')

response = bridge_mgr_rpc_client.send_data('30')

print " [.] Got %s" % (response,)
