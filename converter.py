#%%
import itertools
from pathlib import Path
import re
import shutil
from typing import List, Union

import jinja2

from channels import Channels
from downloader import FileDownloader
from users import Users
from formatter import MessageFormatter


class SlackToHTMLConverter():

    def __init__(self, log_dir: Union[str, Path]) -> None:
        self.log_dir = Path(log_dir)
        self.channels = Channels(self.log_dir)
        self.users = Users(self.log_dir)

    def convert(self, out_dir: Union[Path, str]) -> None:
        out_dir = Path(out_dir)
        for i in self.channels.names:
            # 出力先ディレクトリを作成
            (out_dir / i).mkdir(exist_ok=True, parents=True)
            messages = self._read_channel_messages(i)
            # CSSをコピー
            shutil.copy(
                "./templates/styles.css", str(Path(out_dir) / i / "styles.css")
            )
            # 各月のログを変換。
            for month in messages:
                with (Path(out_dir) / i / f"{month}.html").open("w") as f:
                    f.write(self._render_monthly_messages(messages[month]))
                FileDownloader.download_files(out_dir, messages[month])

    def _render_monthly_messages(self, messages: dict):
        loader = jinja2.FileSystemLoader("./templates")
        env = jinja2.Environment(loader=loader)
        template = env.get_template("monthly_messages.j2")
        output = template.render(messages = messages)
        return output

    def _read_channel_messages(self, name: str) -> List[dict]:
        messages = self.channels[name].messages
        monthly_messages = {
            k: list(itertools.chain.from_iterable([i[1] for i in v]))
            for k, v in itertools.groupby(
                messages.items(), lambda x: re.sub("-[0-9]{2}$", "", x[0])
            )
        }
        return {
            k: MessageFormatter.format(v, self.users)
            for k, v in monthly_messages.items()
        }
