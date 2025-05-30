from sqlalchemy import Column, Integer, String, DateTime, Boolean
from DB.settings import Base, engine

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, nullable=True, default=DateTime)
    updated_at = Column(DateTime, nullable=True, default=DateTime)

    def __init__(self, project_id, task_name, description=None, is_completed= False):
        self.project_id = project_id
        self.task_name = task_name
        self.description = description
        self.is_completed = is_completed
    
if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"テーブルの作成に失敗しました: {e}")