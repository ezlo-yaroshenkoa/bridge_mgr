import argparse
import requests
import ConfigParser

def create_bridge(bridge_name):
    url = get_rest_server_url('bridges/{}').format(bridge_name)

    try:
        response = requests.post(url)
        print response.text
    except requests.RequestException as e:
        print e

def remove_bridge(bridge_name):
    url = get_rest_server_url('bridges/{}'.format(bridge_name))

    try:
        response = requests.delete(url)
        print response.text
    except requests.RequestException as e:
        print e

def get_bridges():
    url = get_rest_server_url('bridges')

    try:
        response = requests.get(url)
        print response.text
    except requests.RequestException as e:
        print e

def get_rest_server_url(request_name):
    config = ConfigParser.RawConfigParser()

    config.read('config.cfg')

    section_name = 'rest_server'

    host = config.get(section_name, 'host')
    port = config.get(section_name, 'port')

    request = 'http://{}:{}/{}'.format(host, port, request_name)

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