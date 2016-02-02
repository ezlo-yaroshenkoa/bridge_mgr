from pecan import expose
from bridges_db import bridges_db

class RootController(object):
    def __init__(self):
        self.bridges_db_ = bridges_db()

    @expose()
    def create_bridge(self, bridge_name):
        self.bridges_db_.add_bridge(bridge_name)
        return 'create bridge %s' % bridge_name

    @expose()
    def remove_bridge(self, bridge_name):
        self.bridges_db_.del_bridge(bridge_name)
        return 'remove bridge %s' % bridge_name

    @expose('json')
    def get_bridges(self):
        return self.bridges_db_.get_bridges()