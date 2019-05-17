# 处理文件的引用
import os
# 分段的引用
import linecache

from bing_translate import bing_auto_to_zh
from bing_translate import bing_auto_to_ja
from bing_translate import bing_auto_to_ko
from bing_translate import bing_auto_to_en

from bd_translate import bd_auto_to_zh
from bd_translate import bd_auto_to_jp
from bd_translate import bd_auto_to_kor
from bd_translate import bd_auto_to_en

# 获取当前文件夹中所有记事本txt文件清单，分段翻译
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))
for fn in fns:
    with open(fn, encoding='utf8') as fp:
        hang = 1    #初始行数设为0
        num_lines = sum(1 for line in open(fn,'rb'))    #文章的实际行数
        while hang < num_lines:
            a1 = str(linecache.getline(fn, hang))
            a1 = a1.replace('\n', '')
            a1 = bing_auto_to_ja(a1, 'auto', 'auto')
            a1 = bd_auto_to_zh(a1)
            print(a1)
            with open('t.txt', 'a+', encoding='utf8') as fp2:
                fp2.write(a1 + '\n')
            hang = hang + 1
    os.remove(fn)
    os.rename('t.txt', fn)
