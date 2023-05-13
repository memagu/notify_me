from dataclasses import dataclass
from typing import Callable, Sequence


@dataclass(frozen=True)
class Option:
    name: str
    callback: Callable
    args: Sequence = tuple()

    def execute(self) -> None:
        self.callback(*self.args)


@dataclass(frozen=True)
class Menu:
    title: str = ""
    description: str = ""
    options: Sequence[Option] = tuple()

    def show(self) -> None:
        if self.title:
            print(self.title, "\n")

        if self.description:
            print(self.description, "\n")

        if self.options:
            print(*(f"{f'{i + 1}.': <{len(str(len(self.options))) + 2}}{option.name}" for i, option in
                    enumerate(self.options)), '', sep='\n')

    def get_option(self) -> Option:
        while True:
            try:
                option_id = int(input("Enter option: ")) - 1
            except ValueError:
                print("Invalid input format, try again.")
                continue

            if not (0 <= option_id < len(self.options)):
                print("Invalid option, try again.")
                continue

            print()
            return self.options[option_id]


class MenuManager:
    def __init__(self, initial_state: Menu = None, transition_map: dict[tuple[Menu, int], Menu] = None):
        self.state = initial_state
        self.transition_map = transition_map

    def transition(self, index: int = 0) -> None:
        self.state = self.transition_map[(self.state, index)]
