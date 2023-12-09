from UI.Events_Menu import Events_Menu

def ui_menu():
    print("")
    print("-------- UI Menu --------")
    print("1. Events menu")
    print("2. Persons menu")
    print("3. Events-Persons menu")
    print("4. Exit")

    choice = int(input("Your choice: "))

    return choice


def run_ui_menu(events_service):
    show_ui_menu = True

    while show_ui_menu:
        x = ui_menu()

        if x == 1:
            Events_Menu.run_events_menu(events_service)

        if x == 4:
            show_ui_menu = False
