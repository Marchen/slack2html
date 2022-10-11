# slack2html: Slack log to HTML converter

[日本語](#インストール)

## Install

slack2html depends `requests` and `jinja2`. Please install them first.

e.g.,

```sh
pip install jinja2 requests
```

or

```sh
conda install jinja2 requests
```

## Usage

```sh
python slack2html.py log_directory output_directory
```

where `log_directory` is the path to the slack log directory (the directory contains `channels.json`) and `output_directory` is the path to the output directory.

## File attachment

*slack2html* downloads all attachment files and store them into the `output_directory/files/FILE_ID` directories.
If a file already exists, *slack2html* skips to download the file therefore using the `output_directory` having downloaded files can save downloading time.

-------------------------------------------------------------------------------

## インストール

slack2htmlは`jinja2`と`requests`に依存しているので、まずこれらのパッケージをインストールしてください。

```sh
pip install jinja2 requests
```

もしくは

```sh
conda install jinja2 requests
```

## つかいかた

```sh
python slack2html.py log_directory output_directory
```

`log_directory`は`channels.json`ファイルがあるSlackのログのディレクトリのパス、 `output_directory`は出力先のディレクトリのパスです。

## 添付ファイル

*slack2html*は全ての添付ファイルをダウンロードし、`output_directory/files/FILE_ID`以下に保存します。すでにファイルが存在する場合、ダウンロードはスキップされるので、ダウンロード時間を節約したいときにはダウンロード済みのファイルが存在する出力フォルダを使ってください。
