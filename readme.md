# slack2html: Slack log to HTML converter

[日本語](#インストール)

## Install

slack2html depends `jinja2`. Please install `jinja2` first.

e.g.,

```sh
pip install jinja2
```

or

```sh
conda install jinja2
```

## Usage

```sh
python slack2html.py log_directory output_directory
```

where `log_directory` is the path to the slack log directory (the directory contains `channel.log`) and `output_directory` is the path to the output directory.

-------------------------------------------------------------------------------

## インストール

slack2htmlは`jinja2`に依存しているので、まず`jinja2`をインストールしてください。

```sh
pip install jinja2
```

もしくは

```sh
conda install jinja2
```

## つかいかた

```sh
python slack2html.py log_directory output_directory
```

`log_directory`は`channel.log`ファイルがあるSlackのログのディレクトリのパス、 `output_directory`は出力先のディレクトリのパスです。
