from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative.base import declared_attr

from db_model import Session, Base


class BaseMixin():

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # def __init__(self, *args, **kwargs):
    # super.__init__(*args, **kwargs)
    # Session()


    def clean(self, session):
        """
        clean table

        Returns:

        TODO: cleanup
        """
        session.execute('''TRUNCATE TABLE {}'''.format(self.__tablename__))
    @classmethod
    def populate(cls, data_list, session):
        for entry in data_list:
            session.merge(cls(**entry))
        session.commit()

    def __repr__(self):
        values = ', '.join("%s=%r" % (n, getattr(self, n)) for n in self.__table__.c.keys())
        return "%s(%s)" % (self.__class__.__name__, values)


class Parent(BaseMixin, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # servers = relationship('Request2Server', back_populates='request')
    # servers = association_proxy('request_servers','server')


    # def __init__(self, session=None, *args, **kwargs):
    #     # self._s = session.query(Server).join(Request2Server).filter(Request2Server.request_rel == self)
    #     self.session = session

    def print_servers(self):
        print('session factory:', Session)
        session = Session()
        print('thread local session:', session)
        session.query(Parent)
        print(self.servers)
        print('sa_instance session:', self._sa_instance_state.session)


