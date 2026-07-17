class PromptChain:

  
    def __init__(self, start: "Prompt"):
        self._current = start

    def run(self) -> None:
        while self._current is not None:
            self._current.display()
            next_prompt = self._current.get_next()
            if callable(next_prompt):
                self._current = next_prompt(self._current.get_user_entry())
            else:
                self._current = next_prompt
