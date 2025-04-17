from sqlalchemy import create_engine, Column, Integer ,String, DateTime
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

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True ,autoincrement=True)
    provider_id = Column(String(255))
    email = Column(String(255))
    name = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, provider_id, email, name, created_at, updated_at):
        self.provider_id = provider_id
        self.email = email
        self.name = name
        self.created_at = created_at
        #現在時刻を取得して、datetime.now()を代入
        self.updated_at = updated_at

try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except Exception as e:
    print(f"Error creating database tables: {e}")