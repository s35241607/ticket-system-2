from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Ticket])
def read_tickets(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Retrieve tickets.
    """
    tickets = crud.ticket.get_multi(db, skip=skip, limit=limit)
    return tickets

@router.post("/", response_model=schemas.Ticket)
def create_ticket(
    *,
    db: Session = Depends(deps.get_db),
    ticket_in: schemas.TicketCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Create new ticket.
    """
    ticket = crud.ticket.create_with_owner(db=db, obj_in=ticket_in, owner_id=current_user.id)
    return ticket

@router.put("/{id}", response_model=schemas.Ticket)
def update_ticket(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    ticket_in: schemas.TicketUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Update a ticket.
    """
    ticket = crud.ticket.get(db=db, id=id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    # Add authorization logic here if needed, e.g., only owner can update
    # if ticket.owner_id != current_user.id:
    #     raise HTTPException(status_code=403, detail="Not enough permissions")
    ticket = crud.ticket.update(db=db, db_obj=ticket, obj_in=ticket_in)
    return ticket

@router.get("/{id}", response_model=schemas.Ticket)
def read_ticket(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Get ticket by ID.
    """
    ticket = crud.ticket.get(db=db, id=id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.delete("/{id}", response_model=schemas.Ticket)
def delete_ticket(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Delete a ticket.
    """
    ticket = crud.ticket.get(db=db, id=id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    # Add authorization logic here
    ticket = crud.ticket.remove(db=db, id=id)
    return ticket
