import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

def create_db(app):
    uri = app.config['SQLALCHEMY_DATABASE_URI']
    engine = sqlalchemy.create_engine(uri)
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return engine
