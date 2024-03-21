from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, MetaData

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String, index=True)
    password = Column(String)
    username = Column(String, unique=True)
    status = Column(String, index=True)
    create_at = Column(String)
