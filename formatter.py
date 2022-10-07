import datetime
import re
from typing import Dict, List

from users import Users


class MessageFormatter():

    @classmethod
    def format(
        cls, monthly_messages: Dict[str, List[dict]], users: Users
    ) -> List[dict]:
        return cls._format_messages_for_html(cls(), monthly_messages, users)

    def _format_messages_for_html(
        self, messages: List[dict], users: Users
    ) -> List[dict]:
        result = {}
        for month in messages:
            result[month] = [
                {
                    "text": self._format_text(m["text"], users),
                    "user": users.find_user_name(m["user"]),
                    "ts": self._format_date(m["ts"]),
                    "files": self._format_files(m)
                }
                for m in messages[month]
            ]
        return result

    def _format_text(self, text: str, users: Users) -> str:
        text = self._format_user_name(text, users)
        text = self._format_page_break(text)
        text = self._format_link(text)
        return text

    def _format_user_name(self, text: str, users: Users) -> str:
        users_place_holder = list(set(re.findall(r"<@[A-Z0-9]{1,}>", text)))
        replace = [
            users.find_user_name(i[2:(len(i) - 1)]) for i in users_place_holder
        ]
        for exp, rep in zip(users_place_holder, replace):
            text = re.sub(exp, rep, text)
        return text

    def _format_page_break(self, text: str) -> str:
        return re.sub(r"\n", "<br />", text)

    def _format_link(self, text: str) -> str:
        return re.sub(r"<http([^>]*)>", r'<a href="http\1">http\1</a>', text)

    def _format_date(self, ts: str) -> str:
        dt = datetime.datetime.fromtimestamp(float(ts))
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def _format_files(self, message):
        if not "files" in message:
            return
        files = list()
        for f in message["files"]:
            if f["mode"] == "tombstone":
                files.append({
                    "id": f["id"], "name": "このファイルは削除されました。",
                    "url": None, "url_private_download": None
                })
            else:
                files.append({
                    "id": f["id"],
                    "name": f["name"],
                    "url": f"../files/{f['id']}/{f['name']}",
                    "url_private_download": self._find_file_url(f)
                })
        return files

    @staticmethod
    def _find_file_url(file: dict):
        if "url_private_download" in file:
            return file["url_private_download"]
        if "":
            return file["external_url"]
