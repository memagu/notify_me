from notification import NotificationManager
from constants import PROJECT_ROOT


def main() -> None:
    notification_manager = NotificationManager(PROJECT_ROOT / "resources/notifications.pkl")
    notification_manager.show()


if __name__ == '__main__':
    main()
