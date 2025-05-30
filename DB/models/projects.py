from sqlalchemy import Column, Integer ,String, DateTime
from DB.settings import Base,engine

class Projects(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True ,autoincrement=True)
    admin_id = Column(String(255),nullable=False)
    project_name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=DateTime,nullable=True)
    updated_at = Column(DateTime, default=DateTime,nullable=True)

    def __init__(self, uid, email, name):
        self.uid = uid
        self.email = email
        self.name = name

if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"テーブルの作成に失敗しました: {e}")