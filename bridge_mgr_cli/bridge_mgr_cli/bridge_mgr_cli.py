import argparse
import requests
import ConfigParser

rest_server_cfg_section = 'rest_server'
rabbit_server_cfg_section = 'rabbit_server'

def create_bridge(bridge_name):
    url = get_rest_server_url('create_bridge')

    data = get_server_host_port(rabbit_server_cfg_section)
    data['bridge_name'] = bridge_name

    response = requests.post(url, data=data)

    print response.text

def remove_bridge(bridge_name):
    url = get_rest_server_url('remove_bridge')

    data = get_server_host_port(rabbit_server_cfg_section)
    data['bridge_name'] = bridge_name

    response = requests.post(url, data=data)

    print response.text

def get_bridges():
    url = get_rest_server_url('get_bridges')
    data = get_server_host_port(rabbit_server_cfg_section)

    response = requests.post(url, data)

    print response.text

def get_rest_server_url(request_name):
    host_port = get_server_host_port(rest_server_cfg_section)

    request = 'http://{0}:{1}/{2}'.format(host_port['host'], host_port['port'], request_name)

    return request

def get_server_host_port(section_name):
    config = ConfigParser.RawConfigParser()
    config.read('config.cfg')

    host = config.get(section_name, 'host')
    port = config.get(section_name, 'port')

    return {'host':host, 'port':port}

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

if __name__ == '__main__':
    parse_cmd_line();
