from __future__ import annotations
from events_and_handlers import events, models
from events_and_handlers import uow


class InvalidSku(Exception):
    pass


def add_batch(
    event: events.BatchCreated,
    uow: uow.AbstractUnitOfWork,
):
    with uow:
        product = uow.products.get(sku=event.sku)
        if product is None:
            product = models.Product(event.sku, batches=[])
            uow.products.add(product)
        product.batches.append(
            models.Batch(event.ref, event.sku, event.qty, event.eta)
        )
        uow.commit()
