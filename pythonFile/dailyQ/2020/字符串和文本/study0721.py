# 你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'#要切割的字符串

result = re.split(r"[;,\.\s]\s*",line)
result2 = re.split(r"(;|,|\s)\s*",line)
# print(result,result2)

import os 
fileNames =os.listdir('.')
# print([n for n in fileNames if n.endswith(('.py',".PY"))])