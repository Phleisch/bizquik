import json
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

with open('db_configuration.json') as db_configuration:
    db_config = json.load(db_configuration)

conn_string = 'postgresql://' + db_config['username'] + ':' \
    + db_config['password'] + '@' + db_config['host'] + '/' \
    + db_config['database']

engine = create_engine(conn_string)
Session = sessionmaker(bind=engine)
Base = declarative_base()
