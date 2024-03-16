from sqlalchemy import and_
from src.database.declarative_base import Session
from src.models.User import User
from src.utils.SecurityUtils import SecurityUtils


class AuthenticationService:

    @classmethod
    def login_user(cls, username, password):
        authenticated_user = Session.query(User).filter(
            and_(
                User.username == username,
                User.password == password
            )
        ).first()

        if authenticated_user:
            return SecurityUtils.generate_token(authenticated_user)

        return None

    @classmethod
    def verify_token(cls, headers):
        return SecurityUtils.verify_token(headers)
