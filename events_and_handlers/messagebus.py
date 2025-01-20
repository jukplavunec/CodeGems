from __future__ import annotations
from events_and_handlers import events
from . import handlers
from events_and_handlers import uow


def handle(
    event: events.Event,
    uow: uow.AbstractUnitOfWork,
):
    results = []
    queue = [event]
    while queue:
        event = queue.pop(0)
        for handler in HANDLERS[type(event)]:
            results.append(handler(event, uow=uow))
            queue.extend(uow.collect_new_events())
    return results


HANDLERS = {
    events.BatchCreated: [handlers.add_batch],
    #TODO: you can add some other events: handlers
}
