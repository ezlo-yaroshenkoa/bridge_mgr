from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Bridge(Base):
    __tablename__ = 'bridge'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)

class bridges_db(object):
    def __init__(self):
        self.engine_ = create_engine('sqlite:///bridges.db')
        self.session_maker_ = sessionmaker()
        self.session_maker_.configure(bind=self.engine_)
        Base.metadata.create_all(self.engine_)

    def add_bridge(self, bridge_name):
        session = self.session_maker_()
        if not session.query(session.query(Bridge).filter_by(name=bridge_name).exists()).scalar():
            bridge = Bridge(name=bridge_name)
            session.add(bridge)
            session.commit()

    def del_bridge(self, bridge_name):
        session = self.session_maker_()
        session.query(Bridge).filter_by(name=bridge_name).delete(synchronize_session=False)
        session.commit()

    def get_bridges(self):
        result = []

        session = self.session_maker_()
        bridges =  session.query(Bridge).all()
        for bridge in bridges:
            result.append(bridge.name)

        return result
