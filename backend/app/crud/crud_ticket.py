from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate

class CRUDTicket(CRUDBase[Ticket, TicketCreate, TicketUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: TicketCreate, owner_id: int
    ) -> Ticket:
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

ticket = CRUDTicket(Ticket)
