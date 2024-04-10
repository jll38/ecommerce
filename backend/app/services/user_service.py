from pydantic import BaseModel
from app.models.sqlalchemy.user import UserModel
from app.db import get_db_session


class User_Service(BaseModel):
    
    def create_user(self, user):
        database = get_db_session()
        user = UserModel(**user)
        database.add(user)
        database.commit()