#%%
import itertools
from pathlib import Path
import shutil
from typing import List, Union

import jinja2

from channels import Channels
from downloader import FileDownloader
from users import Users
from formatter import MessageFormatter
from utils import standardize_file_name

class SlackToHTMLConverter():

    def __init__(self, log_dir: Union[str, Path]) -> None:
        self.log_dir = Path(log_dir)
        self.channels = Channels(self.log_dir)
        self.users = Users(self.log_dir)

    def convert(self, out_dir: Union[Path, str]) -> None:
        out_dir = Path(out_dir)
        out_dir.mkdir(exist_ok=True, parents=True)
        # Copy CSS.
        shutil.copy(
            "./templates/styles.css", str(Path(out_dir) / "styles.css")
        )
        for i in self.channels.names:
            messages = self._read_channel_messages(i)
            formatted_messages = MessageFormatter.format(messages, self.users)
            html_path = Path(out_dir) / standardize_file_name(f"{i}.html")
            with html_path.open("w", encoding="utf_8") as f:
                f.write(self._render_messages(formatted_messages))
            FileDownloader.download_files(out_dir, formatted_messages)

    def _render_messages(self, messages: dict):
        loader = jinja2.FileSystemLoader("./templates")
        env = jinja2.Environment(loader=loader)
        template = env.get_template("channel.j2")
        output = template.render(messages = messages)
        return output

    def _read_channel_messages(self, name: str) -> List[dict]:
        messages = self.channels[name].messages
        return list(itertools.chain.from_iterable(messages.values()))
