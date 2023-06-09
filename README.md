# Pinyin Converter

Simple command-line tool that converts Chinese characters to Pinyin. It processes each line of input separately and prints both the original text and the Pinyin conversion.

## Usage

To use this script, provide a string of Chinese characters as an argument when running the script from the command line. Separate each line of text with two newline characters (`\n\n`).

For example, you could run the script as follows:

```shell
python3 pinyin.py $'你好\n\n世界'
```

This will output:

```
你好
ni hao

世界
shi jie
```

The `$'...'` syntax is used in the command to allow the `\n\n` newline characters to be interpreted correctly by the shell.

## Dependencies

The script uses the `jieba` and `pypinyin` libraries for processing the Chinese characters. Make sure you install these Python packages before running the script.

```shell
pip3 install jieba pypinyin
```
