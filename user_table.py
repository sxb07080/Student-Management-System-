import hashlib
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base = declarative_base()
meta = base.metadata

class Users(base):
    __tablename__ = 'users'
    name = Column(String(32), primary_key=True, nullable=False)
    password = Column(String(512))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return f'name:{self.name}, password:{self.password}'

    def __repr__(self):
        return f'user({self.name!r}, {self.password!r}'

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///users.db')
    # meta.create_all(engine) # run this statement only once to create databse
    return engine

def init_db():
    pass

u_session = sessionmaker(bind=create_db())()

def add_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    try:
        new_user = Users(name=username, password=hashed_password)
        u_session.add(new_user)
        u_session.commit()
    except IntegrityError:
        u_session.rollback()
        raise
    finally:
        u_session.close()

def update_user_password(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    user = u_session.query(Users).filter_by(name=username).first()

    if user:
        user.password = hashed_password
        u_session.commit()
        u_session.close()
    else:
        raise Exception("User not found")

def validate_credentials(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    user = u_session.query(Users).filter_by(name=username, password=hashed_password).first()
    u_session.close()
    return user is not None


if __name__ == '__main__':
    init_db()
