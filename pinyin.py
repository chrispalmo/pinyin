import sys
from pypinyin import lazy_pinyin, Style
import jieba

def chinese_to_pinyin(text):
    seg_list = jieba.cut(text, cut_all=False)
    result = lazy_pinyin("".join(seg_list), style=Style.TONE3)
    return ' '.join(result).lstrip()

def create_html_file(output):
    template = '''<html>
    <head>
    <meta charset="utf-8">
    <title>Pinyin</title>
    <meta name="theme-color" content="#fafafa">
    </head>
    <body style="background-color: black; color: white">
    <div style="white-space: pre-wrap">
    {}
    </div>
    </body>
    </html>'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template.format(output))

if len(sys.argv) > 1:
    # Check if --html is in the arguments
    html_flag = '--html' in sys.argv
    # Remove the --html flag from arguments to leave only the text
    text = ' '.join(arg for arg in sys.argv[1:] if arg != '--html')
    
    lines = text.split('\n')  # split the text into lines by "newlines"
    output = ''
    for line in lines:
        pinyin = chinese_to_pinyin(line)
        output += line + '\n' + pinyin + '\n'  # construct the output
    
    if html_flag:
        create_html_file(output)
    else:
        print(output)
else:
    print("Please provide Chinese text as an argument.")
