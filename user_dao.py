# Database Access Object for the users table of bizquik's database
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from base import Base

class User(Base):
    __tablename__ = 'users'

    id              = Column(Integer, primary_key=True)
    username        = Column(String(100))
    password_salt   = Column(String(100))
    password        = Column(String(100))
    first_name      = Column(String(100))
    last_name       = Column(String(100))
    email           = Column(String(255))

    # The server handles time stamping for when a user object is added to users
    date_created    = Column(DateTime, server_default=func.now())

    def __init__(self, username, password_raw, first_name, last_name, email):
        self.username       = username
        self.password_salt  = generate_salt()
        self.password       = generate_hash(password_raw, password_salt)
        self.first_name     = first_name
        self.last_name      = last_name
        self.email          = email

    # String representation of this object
    def __repr__(self):
        return "<User(username = '%s', full name = '%s %s', email = '%s')>" \
            % (self.username, self.first_name, self.last_name, self.email)

# Return whether or not the given username is unique within the users table
def user_is_unique(name, session):
    # Check each username in the 'users' table against the username passed.
    # Usernames are case insensitive
    first_result = session.query(User).filter(func.lower(User.username) \
                    == name).first()
    return first_result == None
