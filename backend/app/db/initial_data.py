import logging

from app.crud import crud_user
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.schemas.user import UserCreate
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db() -> None:
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    user = crud_user.user.get_by_email(db, email="admin@example.com")
    if not user:
        user_in = UserCreate(
            email="admin@example.com",
            password="password" # In a real app, use a more secure password or secrets management
        )
        user = crud_user.user.create(db, obj_in=user_in)
        logger.info("Created first superuser")
    else:
        logger.info("Superuser already exists in database.")

    db.close()

def main() -> None:
    logger.info("Creating initial data")
    init_db()
    logger.info("Initial data created")

if __name__ == "__main__":
    main()
