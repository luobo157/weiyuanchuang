# -*- coding: utf-8 -*-
# 版本为python3，如果为python2需要在字符串前面加上u
# 检测段落，段落小于5，执行中文分句


import os
import re

def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
        # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
        # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

#获取当前文件夹中所有记事本txt文件清单
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))
for fn in fns:
    num_lines = sum(1 for line in open(fn,'rb')) #'rb'也可以替换为'r', encoding='UTF-8'
    if num_lines < 6:
        #读取文件，小于等于5行的，用函数分割
        with open(fn) as f:
            para = f.read()
            sents = cut_sent(para)
        # 将分割后的内容以覆盖的方式'w'写入
        with open(fn,'w') as f:
            f.write("\n".join(sents))
    else:
        pass
    
