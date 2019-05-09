# -*- coding: utf-8 -*-
#暂时只能执行当前文件夹下的txt文件
#此程序只是替换掉了多余的换行，删除了多余的空格

import os

def alter(file, old_str, new_str):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

fns = (fn for fn in os.listdir() if fn.endswith('.txt'))

for fn in fns:
    try:
        # 此处写入需要替换的代码，空格" ",两个空格"  ",空字符"",换行符号"\n",全角空格"\u3000"多被用来执行首行缩进，tab制表符"\t"
        # 1.把所有空格替换成空字符
        # 2.把所有全角空格替换成空字符
        # 3.把所有换行符替换成空格
        # 4.把两个空格替换成一个空格，多执行几次，就只剩下一个空格了
        # 5.然后把空格替换成换行符号
        alter(fn, " ", "")
        alter(fn, "\u3000", "")
        alter(fn, "\n", " ")
        alter(fn, "  ", " ")
        alter(fn, "  ", " ")
        alter(fn, "  ", " ")
        alter(fn, " ", "\n")
    except:
        pass
    
