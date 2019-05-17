# 伪原创相关

基本思路
--

1.检测指定文件夹所有文件，读取所有txt或者word文件，并将其转换为utf8编码格式

ChangeEncodingToUtf8_3.py

ChangeEncodingToutf8.py

ChangeEncodingToutf8_2.py
均可用

2.检测文件字数，不足700字节（300字）的文件舍弃跳过

deleteNotEnoughWords.py可用

3.删除多余的空格，制表符，全角空格，换行符号

deleteSpacebarAndN.py可用

4.检测行数，如果行数小于5行，执行4.1。行数大于5行，执行5

>4.1使用zh_cut.py进行中文分句

5.读取当前文件夹内的所有txt文件

>5.1读取txt文件的所有段落（line），包括文件标题，按段落强制转换为string类型，分别进行赋值

>5.2段落（包含标题）随机选择翻译软件翻译成日文，韩文，英文，赋值回当前字符串

>5.3段落（包含标题）随机选择翻译软件翻译为中文

>5.4新建t.txt，将翻译再翻译后的段落以"a+"增加写入的方式写入t.txt

>5.5循环到下一个段落，重复5.2，直到所有段落都读取完毕

5.6移除原文件，将t.txt重命名为原文件名

6.读取下一个txt文件，重复5.1


其他
--
bd_translate.py

bing_translate.py

这两个文件封装着百度翻译和必应翻译函数，在main.py中会被引用到

/article，这个文件夹本来是准备作为指定文件夹来存放txt文件的，然而并没有做出来

/fanyishili，找到的一些翻译示例，但是并未整合出来变成可用的
