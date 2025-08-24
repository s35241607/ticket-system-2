import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.crud import crud_user
from app.db.base import Base
from app.schemas.user import UserCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(engine) -> None:
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    user = crud_user.user.get_by_email(db, email="admin@example.com")
    if not user:
        user_in = UserCreate(
            email="admin@example.com",
            password="password"
        )
        user = crud_user.user.create(db, obj_in=user_in)
        logger.info("Created first superuser")
    else:
        logger.info("Superuser already exists in database.")

    db.close()
