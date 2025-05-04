from app.DB.settings import db_session
from app.DB.models.users import Users
from datetime import datetime

class UserController:
    def __init__(self):
        self.db_session = db_session

    def close(self):
        self.db_session.close()

    def get_user(self, user_id):
        user = self.db_session.query(Users).filter(Users.provider_id == user_id).first()
        return user

    def create_user(self, provider_id, email, name):
        created_at = datetime.now()
        updated_at = datetime.now()
        existing_user = self.db_session.query(Users).filter(Users.provider_id == provider_id).first()
        if existing_user:
            existing_user.email = email
            existing_user.name = name
            existing_user.updated_at = updated_at
            self.db_session.commit()
            return existing_user
        new_user = Users(provider_id=provider_id, email=email, name=name, created_at=created_at, updated_at=updated_at)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user