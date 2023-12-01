class EventRepository:
    def __init__(self):
        self._all_events = {}

    def add_event(self, event):
        self._all_events[event.get_id()] = event

    def update_event(self, event):
        self._all_events[event.get_id()] = event

    def delete_event(self, id):
        del self._all_events[id]

    def find_by_id(self, id):
        return self._all_events[id]

    def get_all_events(self):
        return self._all_events
