import os 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {} 

engine = create_engine(DATABASE_URL, connect_args=connect_args) 
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)