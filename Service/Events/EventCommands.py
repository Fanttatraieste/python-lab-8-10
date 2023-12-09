from Domain import Event

class EventCommands:
    def __init__(self, event_repository):
        self._event_repository = event_repository

    def add_event(self, id, date, hour, description):
        event = Event.Event(id, date, hour, description)
        self._event_repository.add_event(event)

    def update_event(self, id, date, hour, description):
        event = Event.Event(id, date, hour, description)
        self._event_repository.update_event(event)

    def delete_event(self, id):
        self._event_repository.delete_event(id)

