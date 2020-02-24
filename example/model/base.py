from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_base():
    return {'base': Base, 'sqlalchemy_url': 'sqlite:///demo.db'}