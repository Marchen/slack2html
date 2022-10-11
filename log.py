import json
from pathlib import Path
from typing import Union


class LogFile():

    """
    Properties:
        log_file_path (Path):
            Path of the log file.
        messages (dict):
            Messages in the log file.
    """

    def __init__(self, log_file_path: Union[str, Path]) -> None:
        self.log_file_path = Path(log_file_path)
        self._load()

    #--------------------------------------------------------------------------
    def _load(self) -> None:
        with self.log_file_path.open(encoding="utf_8") as f:
            self.messages = json.load(f)
