import json
from pathlib import Path
from typing import List, Union


class LogFile():

    def __init__(self, log_file_path: Union[str, Path]) -> None:
        self.log_file_path = Path(log_file_path)
        self._load()

    #--------------------------------------------------------------------------
    def _load(self) -> None:
        with self.log_file_path.open() as f:
            self.messages = json.load(f)

    @property
    def formatted_messages(self) -> List[dict]:
        return
