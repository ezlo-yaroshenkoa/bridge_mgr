import argparse
import requests
import ConfigParser

def create_bridge(bridge_name):
    response = requests.post(get_rest_server_url('create_bridge'), data={'bridge_name':bridge_name})
    print response.text

def remove_bridge(bridge_name):
    response = requests.post(get_rest_server_url('remove_bridge'), data={'bridge_name':bridge_name})
    print response.text

def get_bridges():
    response = requests.get(get_rest_server_url('get_bridges.json'))
    print response.text

def get_rest_server_url(request_name):
    config = ConfigParser.RawConfigParser()
    config.read('config.cfg')

    rest_server_section = 'rest_server'

    rest_server_host = config.get(rest_server_section, 'host')
    rest_server_port = config.get(rest_server_section, 'port')

    request = 'http://{0}:{1}/{2}'.format(rest_server_host, rest_server_port, request_name)

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

if __name__ == "__main__":
    parse_cmd_line();
