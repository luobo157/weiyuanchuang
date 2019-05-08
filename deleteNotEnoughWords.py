# -*- coding: utf-8 -*-
# 预处理，首先检测字数，少于300字的，把文件删除掉
# 目前只能处理当前文件夹

import os

#获取当前文件夹中所有记事本txt文件清单
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))

for fn in fns:
    if os.path.getsize(fn) < 700:   #小于700字节的文件，直接删除掉
        os.remove(fn)
    else:
        pass
