from dataclasses import dataclass
from datetime import date


class Event:
    pass

@dataclass
class BatchCreated(Event):
    ref: str
    sku: str
    qty: int
    eta: date | None = None
