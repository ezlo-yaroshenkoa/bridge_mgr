from pecan import expose, response

class RootController(object):
    @expose()
    def create_bridge(self, bridge_name):
        return 'create bridge %s' % bridge_name

    @expose()
    def remove_bridge(self, bridge_name):
        return 'remove bridge %s' % bridge_name

    @expose('json')
    def get_bridges(self):
        return {'bridge_name' : 'wlan0'}