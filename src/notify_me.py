import os

from configure import toggle_autostart
from constants import PROJECT_ROOT
from menu import Menu, MenuManager, Option
from notification import NotificationManager
import notify


def main() -> None:
    menu_manager = MenuManager()
    notification_manager = NotificationManager(PROJECT_ROOT / "resources/notifications.pkl")

    main_menu = Menu(
        "Notify Me",
        "Welcome to Notify Me, a tool for managing simple notifications.",
        options=(
            Option(
                "Configure Notify Me",
                menu_manager.transition,
                (0,)
            ),
            Option(
                "Manage notifications",
                menu_manager.transition,
                (1,)
            ),
            Option(
                "Exit",
                exit
            )
        )
    )
    configure = Menu(
        "Configuration",
        options=(
            Option(
                "Toggle autostart",
                toggle_autostart
            ),
            Option(
                "Return to main menu",
                menu_manager.transition
            )
        )
    )
    manage_notifications = Menu(
        "Manage notifications",
        options=(
            Option(
                "Add a notification",
                notification_manager.prompt_create
            ),
            Option(
                "Remove a notification",
                notification_manager.prompt_remove
            ),
            Option(
                "Test notifications",
                notify.main
            ),
            Option(
                "Return to main menu",
                menu_manager.transition
            )
        )
    )

    menu_manager.state = main_menu
    menu_manager.transition_map = {
        (main_menu, 0): configure,
        (main_menu, 1): manage_notifications,
        (configure, 0): main_menu,
        (manage_notifications, 0): main_menu,
    }

    while True:
        os.system("cls")

        menu_manager.state.show()
        menu_manager.state.get_option().execute()


if __name__ == "__main__":
    main()
