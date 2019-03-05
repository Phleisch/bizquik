# Database Access Object for the users table of bizquik's database
from sqlalchemy import Column, DateTime, Integer, String

class User(db):
    __tablename__ = 'users'

    id            = Column(Integer, primary_key=True)
    username      = Column(String)
    password_salt = Column(String)
    password      = Column(String)
    first_name    = Column(String)
    last_name     = Column(String)
    email         = Column(String)
    date_created  = Column(DateTime)
