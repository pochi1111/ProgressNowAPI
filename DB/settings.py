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

print(f"DB_USER: {user}, PASSWORD: {password}, HOST: {host}, DATABASE: {db_name}")

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db_name}')

db_session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  )
)

Base = declarative_base()
Base.query = db_session.query_property()