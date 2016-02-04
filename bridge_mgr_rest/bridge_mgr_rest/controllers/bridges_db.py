import sqlite3

class bridges_db(object):
    def __init__(self):
        self.connection_ = sqlite3.connect('bridges.db')
        self.connection_.execute('create table if not exists bridges(bridge_name text primary key)')

    def __del__(self):
        self.connection_.close()

    def add_bridge(self, bridge_name):
        self.connection_.execute("insert or ignore into bridges(bridge_name) values('{0}')".format(bridge_name))
        self.connection_.commit()

    def del_bridge(self, bridge_name):
        self.connection_.execute("delete from bridges where bridge_name='{0}'".format(bridge_name))
        self.connection_.commit()

    def get_bridges(self):
        cursor = self.connection_.execute('select bridge_name from bridges')
        result = cursor.fetchall()
        data = []

        for item in result:
            data.append(item[0])

        return data