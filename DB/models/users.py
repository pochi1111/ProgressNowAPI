from sqlalchemy import Column, Integer ,String, DateTime
from DB.settings import Base,engine

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True ,autoincrement=True)
    provider_id = Column(String(255),nullable=False)
    uid = Column(String(255), unique=True, nullable=False)
    email = Column(String(255),nullable=False)
    name = Column(String(255),nullable=False)
    created_at = Column(DateTime, default=DateTime,nullable=False)
    updated_at = Column(DateTime, default=DateTime,nullable=False)

    def __init__(self, provider_id, uid, email, name, created_at, updated_at):
        self.provider_id = provider_id
        self.uid = uid
        self.email = email
        self.name = name
        self.created_at = created_at
        #現在時刻を取得して、datetime.now()を代入
        self.updated_at = updated_at

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"テーブルの作成に失敗しました: {e}")