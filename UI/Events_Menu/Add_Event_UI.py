from Service.Events import EventService

def ui_add_event_menu(events_service):
    print("")
    print("-------- Add Events Menu --------")
    id = int(input(" id: "))
    date = input(" date: ")
    hour = int(input(" hour: "))
    description = input(" description: ")

    events_service.add_event(id, date, hour, description)

def run_add_event_menu(events_service):
    ui_add_event_menu(events_service)

