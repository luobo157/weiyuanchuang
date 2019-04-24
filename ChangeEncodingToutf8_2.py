#方法二,批量改变当前文件夹里txt文件的编码为utf8
#同样只对中文txt有效

from os import listdir

fns = (fn for fn in listdir() if fn.endswith('.txt'))

for fn in fns:
    with open(fn,'rb+') as fp:
        content = fp.read()
        try:
            #尝试使用utf8编码
            content.decode('utf8')
        except:
            #使用gbk解码后再使用utf8编码，写回文件
            content = content.decode('gbk').encode('utf8')
            fp.seek(0)
            fp.write(content)
