from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import get_settings

# This will be populated by the application startup event
engine = None
SessionLocal = None

def get_db():
    if SessionLocal is None:
        raise Exception("Database not initialized")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
