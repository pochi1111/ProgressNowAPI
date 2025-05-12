from DB.settings import db_session
from DB.models.users import Users
from datetime import datetime

class UserController:
    def __init__(self):
        self.db_session = db_session

    def close(self):
        self.db_session.close()

    #get userinfo by email
    def get_user(self, email):
        user = self.db_session.query(Users).filter(Users.email == email).first()
        return user

    #get userinfo by uid
    def get_user_by_uid(self, uid):
        user = self.db_session.query(Users).filter(Users.uid == uid).first()
        return user

    def create_user(self, uid, email, name):
        created_at = datetime.now()
        updated_at = datetime.now()
        existing_user = self.db_session.query(Users).filter(Users.email == email).first()
        if existing_user:
            existing_user.uid = uid
            existing_user.email = email
            existing_user.name = name
            existing_user.updated_at = updated_at
            self.db_session.commit()
            return existing_user
        new_user = Users(email=email, uid=uid,  name=name, created_at=created_at, updated_at=updated_at)
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def delete_user(self, uid):
        user = self.db_session.query(Users).filter(Users.uid == uid).first()
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            return True
        return False