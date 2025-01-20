from datetime import date
from pydantic import BaseModel


class BatchCreated(BaseModel):
    ref: str
    sku: str
    qty: int
    eta: date | None = None
