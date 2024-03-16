from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database.declarative_base import Base
from src.models.Role import Role


class User(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column("pass", String)
    role_id = Column(ForeignKey("app_role.id"))
    fullname = Column(String)

    role = relationship('Role', back_populates="users")



