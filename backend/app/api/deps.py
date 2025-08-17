from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from typing import Annotated

from app.db.session import get_db
from app.crud import crud_user
from app.models.user import User

# In a real scenario with Kong, Kong would validate the JWT
# and pass user info (e.g., user ID) in a trusted header.
# This dependency simulates that. For development, we can pass a default user ID.
def get_current_user(
    db: Session = Depends(get_db),
    x_user_id: Annotated[int, Header()] = 1 # Default to user 1 for dev
) -> User:
    user = crud_user.user.get(db, id=x_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # In a full JWT implementation, you would decode the token here
    # and get the user ID from the token's subject.

    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
