from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

from app.models.ticket import TicketStatus, TicketPriority
from .user import User

# Shared properties
class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[TicketPriority] = TicketPriority.MEDIUM

# Properties to receive on item creation
class TicketCreate(TicketBase):
    pass

# Properties to receive on item update
class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TicketPriority] = None
    status: Optional[TicketStatus] = None
    approver_id: Optional[int] = None

# Properties shared by models in DB
class TicketInDBBase(TicketBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    status: TicketStatus
    owner_id: int
    owner: User

    model_config = ConfigDict(from_attributes=True)

# Properties to return to client
class Ticket(TicketInDBBase):
    pass

# Properties stored in DB
class TicketInDB(TicketInDBBase):
    pass
