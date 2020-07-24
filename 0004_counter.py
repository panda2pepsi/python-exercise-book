# -*-coding:utf-8-*-

# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
from collections import Counter

def count_words(filename):
    txt = ""
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                txt += line
    except FileNotFoundError:
        pass
    res = re.split(
        r"[\~\`\!\@\#\$\%\^\&\*\(\)\+\=\{\}\;\:\'\"\<\>\,\.\?\\\/\…\s\d]+", txt)

    # if re matches the final character, it will return a None str
    # so we need to remove it
    words_res = [x.lower() for x in res if x != '']
    count = Counter(words_res)
    print(count)
    
count_words("0004_words_input.txt")

