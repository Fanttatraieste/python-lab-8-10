from UI.Events_Menu import Add_Event_UI

def ui_events_menu():
    print("")
    print("-------- Events Menu --------")
    print("1. Add new event")
    print("2. Update event")
    print("3. Delete Event")
    print("4. Get Event")
    print("5. Go back")

    choice = int(input("Your choice: "))

    return choice

def run_events_menu(events_service):
    show_events_menu = True

    while show_events_menu:
        x = ui_events_menu()

        if x == 1:
            Add_Event_UI.run_add_event_menu(events_service)

        if x == 5:
            show_events_menu = False
