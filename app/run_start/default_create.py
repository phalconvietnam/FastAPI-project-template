#import faker.providers
from app.helpers.enums import UserRole
from app.models.model_user import User
from fastapi_sqlalchemy import db
from app.core.security import get_password_hash

#fake = faker.Faker()


class DefaultUser:
    def user(data={}): 
        user = User(
            full_name=data.get('full_name'),
            email=data.get('email'),
            hashed_password=get_password_hash(data.get('password')),
            is_active=data.get('is_active') if data.get('is_active') is not None else True,
            role=data.get('role') if data.get('role') is not None else UserRole.GUEST.value
        )
        with db():
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
        print ("insert first user")