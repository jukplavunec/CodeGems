from datetime import datetime
from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK

from events_and_handlers.schemas import BatchCreated
from events_and_handlers import events, messagebus, uow

app = FastAPI(description='Events Example API')

@app.post("/add_batch")
async def add_batch(request: BatchCreated) -> None:
    eta = request.eta
    if eta is not None:
        eta = datetime.fromisoformat(eta).date()
    event = events.BatchCreated(ref=request.ref, sku=request.sku, qty=request.qty, eta=eta)
    messagebus.handle(event, uow.SqlAlchemyUnitOfWork())
    return Response(status_code=HTTP_200_OK)
