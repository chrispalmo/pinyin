import sys
from pypinyin import lazy_pinyin, Style
import jieba

def chinese_to_pinyin(text):
    seg_list = jieba.cut(text, cut_all=False)
    result = lazy_pinyin("".join(seg_list), style=Style.TONE3)
    return ' '.join(result)

if len(sys.argv) > 1:
    text = sys.argv[1]
    lines = text.split('\n\n')  # split the text into lines by "double newlines"
    for line in lines:
        pinyin = chinese_to_pinyin(line)
        print(line)  # print the original line
        print(pinyin)  # print the converted pinyin
        print()  # print a newline
else:
    print("Please provide Chinese text as an argument.")
