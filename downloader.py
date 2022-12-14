from pathlib import Path
import requests
from typing import List

from utils import standardize_file_name

class FileDownloader():

    @classmethod
    def download_files(cls, out_dir: Path, messages: List[dict]) -> None:
        for i in messages:
            if i["files"] is None:
                continue
            for f in i["files"]:
                if f["url_private_download"] is None:
                    continue
                file_name = standardize_file_name(f["name"])
                out_path: Path =  out_dir / "files" / f["id"] / file_name
                if out_path.exists():
                    continue
                r = requests.get(
                    f["url_private_download"], allow_redirects=True
                )
                out_path.parent.mkdir(exist_ok=True, parents=True)
                with out_path.open("wb") as f:
                    f.write(r.content)
