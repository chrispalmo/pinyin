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

### HTML Output

To generate an `index.html` file with the pinyin conversion result, add `--html` flag either before or after the Chinese text in your command.

For example:

```bash
python3 pinyin.py --html $'你好\n世界'
```

or

```bash
python3 pinyin.py $'你好\n世界' --html
```

In both cases, an `index.html` file will be created in the same directory as your script. The output will be formatted such that each line of Chinese text will be immediately followed by its pinyin equivalent, preserving the structure of the input.

Note: If the `index.html` file already exists, running the command with `--html` flag will overwrite the existing file with the new content.

## Dependencies

The script uses the `jieba` and `pypinyin` libraries for processing the Chinese characters. Make sure you install these Python packages before running the script.

```shell
python3 -m pip install jieba pypinyin
```
