import re
import unicodedata


def standardize_file_name(file_name: str) -> str:
    """
    Standardize file name

    Args:
        file_name (str): file name.

    Returns:
        str: Standardized file name.
    """
    file_name = unicodedata.normalize("NFC", file_name)
    forbidden = {
        r":": "：",
        r"\?": "？",
        r"\\": "＼",
        r"/": "／",
        r"\*": "＊",
        r"<": "＜",
        r">": "＞",
        r"\|": "｜"
    }
    for pattern, replace in forbidden.items():
        file_name = re.sub(pattern, replace, file_name)
    return file_name
