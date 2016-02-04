from pecan import expose, abort
from bridges_db import bridges_db
from bridge_mgr_rpc_client import BridgeManagerRpcClient
import json

class RootController(object):
    def __init__(self):
        self.bridges_db_ = bridges_db()
        self.bridge_mgr_rpc_client_ = BridgeManagerRpcClient()

    @expose(generic=True)
    def bridges(self):
        return self.bridges_db_.get_bridges()

    @bridges.when(method='POST')
    def create_bridge(self, bridge_name):
        data = {}
        data['action'] = 1
        data['bridge_name'] = bridge_name
        json_data = json.dumps(data)

        if self.bridge_mgr_rpc_client_.send_data(json_data):
            self.bridges_db_.add_bridge(bridge_name)
        else:
            abort(500)

        return 'bridge {0} added'.format(bridge_name)

    @bridges.when(method='DELETE')
    def remove_bridge(self, bridge_name):
        data = {}
        data['action'] = 0
        data['bridge_name'] = bridge_name
        json_data = json.dumps(data)

        if self.bridge_mgr_rpc_client_.send_data(json_data):
            self.bridges_db_.del_bridge(bridge_name)
        else:
            abort(500)

        return 'bridge {0} deleted'.format(bridge_name)