from pecan import expose, redirect

class RootController(object):
    @expose(method='POST')
    def create_bridge(self, bridge_name):
        return 'create bridge %s' % bridge_name

    @expose(method='POST')
    def remove_bridge(self, bridge_name):
        return 'remove bridge %s' % bridge_name

    @expose(method='GET')
    def get_bridges(self):
        return 'get bridges'