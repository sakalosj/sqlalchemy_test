from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



# e = create_engine("sqlite:///datafiles/data.sqlite", connect_args={'check_same_thread': False})
e = create_engine('mysql+pymysql://qualys:123456@localhost/qualys_scan')
Base = declarative_base()
Base.metadata.create_all(e)
# Session = scoped_session(sessionmaker(bind=engine))

Session = sessionmaker(bind=e)