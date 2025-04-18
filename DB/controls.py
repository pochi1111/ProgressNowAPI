from DB.settings import db_session
from DB.models.users import Users
from datetime import datetime

class UserController:
    def __init__(self):
        self.db_session = db_session

    def get_user(self, user_id):
        user = self.db_session.query(Users).filter(Users.provider_id == user_id).first()
        return user

    def create_user(self, provider_id, email, name):
        created_at = datetime.now()
        updated_at = datetime.now()
        existing_user = self.db_session.query(Users).filter(Users.provider_id == provider_id).first()
        if existing_user:
            raise Exception("409:User already exists")
        new_user = Users(provider_id=provider_id, email=email, name=name, created_at=created_at, updated_at=updated_at)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user