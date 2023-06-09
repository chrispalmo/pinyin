import sys
from pypinyin import lazy_pinyin, Style
import jieba

def chinese_to_pinyin(text):
    seg_list = jieba.cut(text, cut_all=False)
    result = lazy_pinyin("".join(seg_list), style=Style.TONE3)
    return ' '.join(result)

if len(sys.argv) > 1:
    print(chinese_to_pinyin(sys.argv[1]))
else:
    print("Please provide Chinese text as an argument.")

