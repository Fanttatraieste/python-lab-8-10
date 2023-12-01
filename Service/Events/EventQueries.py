class EventQueries:
    def __init__(self, event_repository):
        self._event_repository = event_repository

    def get_event_by_id(self, id):
        return self._event_repository.find_by_id(id)

    def get_all_events(self):
        return self._event_repository.get_all_events()

    def filter_events_by_field(self, field, value):
        output_events = {}

        for event in self._event_repository.get_all_events():
            if field == 'date':
                if event.get_date() == value:
                    output_events[event.get_id()] = event
            if field == 'hour':
                if event.get_hour() == value:
                    output_events[event.get_id()] = event
            if field == 'description':
                if event.get_description() == value:
                    output_events[event.get_id()] = event

        return output_events

