from UI import UI_menu
from Service.Events import EventService

def __main__():
    events_service = EventService.EventService()

    UI_menu.run_ui_menu(events_service)

__main__()
