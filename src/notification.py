from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from pickle import load, dump

from winotify import Notification

from constants import APP_NAME, PROJECT_ROOT


@dataclass
class NotificationData:
    title: str
    msg: str
    due_date: datetime

    def build(self) -> Notification:
        return Notification(
            app_id=APP_NAME,
            title=f"{self.title} | {self.due_date.strftime('%Y-%m-%d %H:%M')}",
            msg=f"{self.msg}\n\nDue in: {self.due_date - datetime.now()}",
            icon=PROJECT_ROOT / "resources/icon.png",
            duration="short"
        )


class NotificationManager:
    def __init__(self, path: Path):
        self.path = path
        self.notifications: list[NotificationData]

        try:
            self.notifications = self.load()
        except FileNotFoundError or EOFError:
            self.notifications = list()

    def load(self) -> list[NotificationData]:
        with open(self.path, "rb") as f:
            return load(f)

    def save(self) -> None:
        with open(self.path, "wb") as f:
            dump(self.notifications, f)

    def add(self, notification_data: NotificationData) -> None:
        self.notifications.append(notification_data)
        self.save()

    def remove(self, notification_data: NotificationData) -> None:
        self.notifications.remove(notification_data)
        self.save()

    def show(self) -> None:
        for notification_data in self.notifications:
            notification_data.build().show()

    def prompt_create(self) -> None:
        title = input("Enter notification title: ")
        msg = input("Enter notification message: ")

        while True:
            try:
                due_date = datetime.strptime(input("Enter notification due date (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("Invalid date format, try again.")

        self.add(NotificationData(title, msg, due_date))

    def print_notification_list(self) -> None:
        print(
            *(f"{f'{i + 1}.': <{len(str(len(self.notifications))) + 2}}{notification_data.title}"
              for i, notification_data in enumerate(self.notifications)), '', sep='\n'
        )

    def get_notification(self) -> NotificationData:
        while True:
            try:
                notification_id = int(input("Enter notification id: ")) - 1
            except ValueError:
                print("Invalid input format, try again.")
                continue

            if not (0 <= notification_id < len(self.notifications)):
                print("Invalid notification id, try again.")
                continue

            return self.notifications[notification_id]

    def prompt_remove(self) -> None:
        if not self.notifications:
            return

        self.print_notification_list()
        self.remove(self.get_notification())
