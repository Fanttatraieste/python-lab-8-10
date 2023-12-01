from Service.Events import EventCommands, EventQueries
from Repository import EventRepository

class EventService:
    def __init__(self):
        self._event_repository = EventRepository()
        self._event_commands = EventCommands(self._event_repository)
        self._event_queries = EventQueries(self._event_repository)

    def add_event(self, id, date, hour, description):
        self._event_commands.add_event(id, date, hour, description)

    def update_event(self, id, date, hour, description):
        self._event_commands.update_event(id, date, hour, description)

    def delete_event(self, id):
        self._event_commands.delete_event(id)

    def get_event_by_id(self, id):
        return self._event_queries.get_event_by_id(id)

    def get_all_events(self):
        return self._event_queries.get_all_events()

    def filter_events_by_field(self, field, value):
        return self._event_queries.filter_events_by_field(field, value)

    def print_events(self):
        for event in self.get_all_events():
            print("")
            print(event)
            print("")


