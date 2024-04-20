from fastapi import APIRouter, FastAPI


support_router = APIRouter()


@support_router.put('/ticket')  # Modify Ticket Status
def modify_ticket_status():
    pass


@support_router.post('/ticket')  # Submit Ticket
def submit_ticket():
    pass


@support_router.get('/ticket')  # Get Tickets
def read_ticket():
    pass


@support_router.get('/ticket/${ticket_id}')  # Get Ticket By Id
def read_tickets():
    pass
