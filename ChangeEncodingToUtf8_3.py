#方法三
#纯英文，中英混合可用，全英文应该不可用

from os import listdir
from chardet import detect

fns = (fn for fn in listdir() if fn.endswith('.txt'))
for fn in fns:
    with open(fn,'rb+') as fp:
        content = fp.read()
        #判断编码格式
        encoding = detect(content)['encoding']
        #格式转换
        content = content.decode(encoding).encode('utf8')
        #写回文件
        fp.seek(0)
        fp.write(content)
