"""
Define classes handling channels.
"""

# %%===========================================================================
#   Import modules
# =============================================================================
import json
from pathlib import Path
from typing import Any, Dict, List, Union

from log import LogFile


# =============================================================================
class Channel():
    """
    Read data from a channel.
    """

    # -------------------------------------------------------------------------
    def __init__(
        self, log_dir: Union[Path, str], name: str, meta: dict
    ) -> None:
        """
        Initialize.

        Args:
            log_dir (Union[Path, str]):
                path of a directory having log files.
            name (str):
                channel name.
            meta (dict):
                channel meta data.
        """
        self.log_dir = Path(log_dir)
        self.name = name
        self.meta = meta

    # -------------------------------------------------------------------------
    @property
    def log_files(self) -> List[Path]:
        "Paths of all log files."
        return sorted((self.log_dir / self.name).glob("*.json"))

    # -------------------------------------------------------------------------
    def __getitem__(self, key: str) -> Any:
        """
        Returns channel meta data.

        Args:
            key (str):
                name of meta data.

        Returns:
            Any:
                meta data.
        """
        return self.meta[key]

    # -------------------------------------------------------------------------
    @property
    def messages(self) -> Dict[str, List[dict]]:
        """
        Returns all messages.

        Returns:
            Dict[str, List[dict]]:
                {"YYYY-MM-DD": [message1, message2]}
        """
        return {
            str(i.name).replace(".json", ""):
            LogFile(i).messages for i in self.log_files
        }


# =============================================================================
class Channels():
    "Read all channels."

    #--------------------------------------------------------------------------
    def __init__(self, log_dir: Union[Path, str]) -> None:
        self.log_dir = Path(log_dir)
        self._load()

    #--------------------------------------------------------------------------
    def _load(self) -> None:
        with (self.log_dir / "channels.json").open(encoding="utf_8") as f:
            self.channels = json.load(f)

    #--------------------------------------------------------------------------
    @property
    def names(self) -> List[str]:
        return [i["name"] for i in self.channels]

    def __getitem__(self, name: str):
        for i in self.channels:
            if i["name"] == name:
                meta = i
                break
        return Channel(self.log_dir, name, meta)
