#方法一，改变当前文件夹内所有txt的编码
#貌似只对包含中文的txt文件有效果，纯英文无效果好像

import os

#获取当前文件夹中所有记事本txt文件清单
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))
for fn in fns:
    try:
        #首先尝试使用UTF8编码打开并读取文件内容
        #如果失败会抛出异常
        with open(fn, encoding='utf8') as fp:
            fp.read()
    except:
        #以默认的GBK编码读取源文件内容
        #以utf8编码写入新文件
        with open(fn) as fp1:
            with open('t.txt', 'w', encoding='utf8') as fp2:
                fp2.write(fp1.read())
        #删除源文件，把新文件重命名为源文件
        os.remove(fn)
        os.rename('t.txt', fn)
