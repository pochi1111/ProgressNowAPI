from DB.settings import Session
from DB.models.users import Users
from DB.models.projects import Projects
from DB.models.tasks import Tasks
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

class UserController:
    def __init__(self):
        self.db_session = Session()

    def close(self):
        self.db_session.close()

    def get_user_by_id(self, user_id):
        try:
            if not isinstance(user_id, int):
                return None
            return self.db_session.query(Users).filter(Users.id == user_id).first()
        except SQLAlchemyError:
            return None

    def get_user_by_email(self, email):
        try:
            if not isinstance(email, str):
                return None
            return self.db_session.query(Users).filter(Users.email == email).first()
        except SQLAlchemyError:
            return None

    def get_user_by_uid(self, uid):
        try:
            if not isinstance(uid, str):
                return None
            return self.db_session.query(Users).filter(Users.uid == uid).first()
        except SQLAlchemyError:
            return None

    def create_user(self, uid, email, name):
        try:
            if not (isinstance(uid, str) and isinstance(email, str) and isinstance(name, str)):
                return None
            existing_user = self.db_session.query(Users).filter(Users.email == email).first()
            if existing_user:
                existing_user.uid = uid
                existing_user.email = email
                existing_user.name = name
                self.db_session.commit()
                return existing_user
            new_user = Users(email=email, uid=uid, name=name)
            self.db_session.add(new_user)
            self.db_session.commit()
            return new_user
        except SQLAlchemyError:
            self.db_session.rollback()
            return None

    def delete_user(self, uid):
        try:
            if not isinstance(uid, str):
                return 404
            user = self.db_session.query(Users).filter(Users.uid == uid).first()
            if user:
                self.db_session.delete(user)
                self.db_session.commit()
                return 204
            return 404
        except SQLAlchemyError:
            self.db_session.rollback()
            return 500

class ProjectController:
    def __init__(self):
        self.db_session = Session()

    def close(self):
        self.db_session.close()

    def get_project_by_id(self, project_id):
        try:
            if not isinstance(project_id, int):
                return None
            return self.db_session.query(Projects).filter(Projects.id == project_id).first()
        except SQLAlchemyError:
            return None

    def create_project(self, admin_id, project_name):
        try:
            if not (isinstance(admin_id, int) and isinstance(project_name, str)):
                return None
            new_project = Projects(project_name=project_name, admin_id=admin_id)
            self.db_session.add(new_project)
            self.db_session.commit()
            return new_project
        except SQLAlchemyError:
            self.db_session.rollback()
            return None

    def update_project(self, project_id, project_name=None, admin_id=None):
        try:
            if not isinstance(project_id, int):
                return 404
            project = self.db_session.query(Projects).filter(Projects.id == project_id).first()
            if project:
                if project_name and isinstance(project_name, str):
                    project.project_name = project_name
                if admin_id and isinstance(admin_id, int):
                    project.admin_id = admin_id
                project.updated_at = datetime.now()
                self.db_session.commit()
                return project
            else:
                return 404
        except SQLAlchemyError:
            self.db_session.rollback()
            return 500

    def delete_project(self, project_id):
        try:
            if not isinstance(project_id, int):
                return 500
            project = self.db_session.query(Projects).filter(Projects.id == project_id).first()
            if project:
                self.db_session.delete(project)
                self.db_session.commit()
                return 204
            return 404
        except SQLAlchemyError:
            self.db_session.rollback()
            return 500
    
class TaskController:
    def __init__(self):
        self.db_session = Session()

    def close(self):
        self.db_session.close()

    def get_task_by_id(self, task_id):
        try:
            if not isinstance(task_id, int):
                return None
            return self.db_session.query(Tasks).filter(Tasks.id == task_id).first()
        except SQLAlchemyError:
            return None

    def create_task(self, project_id, title, description=None, is_completed=False):
        try:
            if not (isinstance(project_id, int) and isinstance(title, str)):
                return None
            new_task = Tasks(project_id=project_id, title=title, description=description, is_completed=is_completed)
            self.db_session.add(new_task)
            self.db_session.commit()
            return new_task
        except SQLAlchemyError:
            self.db_session.rollback()
            return None

    def update_task(self, task_id, title=None, description=None, is_completed=None):
        try:
            if not isinstance(task_id, int):
                return 404
            task = self.db_session.query(Tasks).filter(Tasks.id == task_id).first()
            if task:
                if title and isinstance(title, str):
                    task.title = title
                if description and isinstance(description, str):
                    task.description = description
                if is_completed is not None:
                    task.is_completed = is_completed
                task.updated_at = datetime.now()
                self.db_session.commit()
                return task
            else:
                return 404
        except SQLAlchemyError:
            self.db_session.rollback()
            return 500

    def delete_task(self, task_id):
        try:
            if not isinstance(task_id, int):
                return 500
            task = self.db_session.query(Tasks).filter(Tasks.id == task_id).first()
            if task:
                self.db_session.delete(task)
                self.db_session.commit()
                return 204
            return 404
        except SQLAlchemyError:
            self.db_session.rollback()
            return 500