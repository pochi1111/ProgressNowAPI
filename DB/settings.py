from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('HOST')
db_name = os.getenv('DB_NAME')


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db_name}')


Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
# Base.query = Session().query_property()