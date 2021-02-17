from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./expense.db"
SQLALCHEMY_DATABASE_URL1 = "sqlite:///./users.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,SQLALCHEMY_DATABASE_URL1,connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()