import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use environment variable for database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

# Handle PostgreSQL URL format (Render provides it with postgres:// which needs to be changed to postgresql://)
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
