#%%
import json
from pathlib import Path
from typing import Union


class Users:

    #--------------------------------------------------------------------------
    def __init__(self, log_dir: Union[Path, str]) -> None:
        self.log_dir = Path(log_dir)
        self._load()

    #--------------------------------------------------------------------------
    def _load(self) -> None:
        with (self.log_dir / "users.json").open(encoding="utf_8") as f:
            self.users = json.load(f)

    def find_user_name(self, id_: str) -> str:
        for i in self.users:
            if i["id"] == id_:
                if i["profile"]["display_name"] != "":
                    return i["profile"]["display_name"]
                if i["profile"]["real_name"] != "":
                    return i["profile"]["real_name"]
        return None
