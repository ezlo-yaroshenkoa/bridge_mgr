from pecan import expose, abort
from bridges_db import bridges_db
from bridge_mgr_rpc_client import BridgeManagerRpcClient

class RootController(object):
    def __init__(self):
        self.bridges_db_ = bridges_db()
        self.bridge_mgr_rpc_client_ = BridgeManagerRpcClient()

    @expose()
    def create_bridge(self, bridge_name):
        data = "{'action':1,'bridge_name':'{0}'}".format(bridge_name)

        if self.bridge_mgr_rpc_client_.send_data(data):
            self.bridges_db_.add_bridge(bridge_name)
        else:
            abort(500)

        return 'create bridge %s' % bridge_name

    @expose()
    def remove_bridge(self, bridge_name):
        data = "{'action':0,'bridge_name':'{0}'}".format(bridge_name)

        if self.bridge_mgr_rpc_client_.send_data(data):
            self.bridges_db_.del_bridge(bridge_name)
        else:
            abort(500)

        return 'remove bridge %s' % bridge_name

    @expose('json')
    def get_bridges(self):
        return self.bridges_db_.get_bridges()