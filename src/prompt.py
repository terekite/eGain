from __future__ import annotations
from constants import QUIT
from constants import MESSAGES


class Prompt:

  
    def __init__(
            self,
            message: str,
            validation: callable = lambda _: True,
            invalid_input_message: str = MESSAGES.INVALID_INPUT_DEFAULT
    ):
        self._message = message
        self._user_entry = None
        self._validation = validation
        self._invalid_input_message = invalid_input_message
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, next_prompt: dict[str, "Prompt"] | "Prompt") -> None:
        if isinstance(next_prompt, dict):
            self._next = lambda key: next_prompt[key]
        else:
            self._next = next_prompt

    def display(self) -> None:
        self._user_entry = input('\n' + self._message)
        self._validate_input()

    def get_user_entry(self) -> str:
        return self._user_entry

    def _validate_input(self) -> None:
        if self._user_entry == QUIT:
            exit()
        if not self._validation(self._user_entry):
            print(self._invalid_input_message)
            self._user_entry = None
            self.display()
