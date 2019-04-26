# 伪原创相关

基本思路
--

1.检测制定文件夹所有文件，读取所有txt或者word文件

2.检测文件字数，不足300字的文件舍弃跳过

3.删除多余的空格，制表符，全角空格，换行符号

4.检测行数，如果行数小于5行，执行4.1。行数大于5行，执行5

>4.1使用zh_cut进行中文分句

5.读取文件所有的段落（line），包括文件标题，按段落分别进行赋值

段落（包含标题）随机选择翻译软件翻译成日文，韩文，英文，赋值回当前字符串

段落（包含标题）随机选择翻译软件翻译为中文

将段落重新按顺序组合起来

6.新建文件夹，将翻译后的，按顺序组合起来的文章保存



相关文件的作用
---
ChangeEncodingToutf8.py

ChangeEncodingToutf8_2.py

ChangeEncodingToutf8_3.py

这三个文件是批量改变当前文件夹内txt文件的编码为utf8，每一个都可用

deleteSpacebarAndN.py

这个文件可以去掉多余的空格和换行

注意：由于并没有限定文件类型，指定的文件加下的所有文件都会被替换掉

BaiduTranslateAutoToAuto.py

bingTranslateAutoToAuto.py

youdaotranslation.py

翻译文件，百度和必应都是封装函数，有道还未封装

百度使用了api，必应使用了模拟访问，有道使用了模拟访问，还附带了反爬？（未知）

zh_cut.py

这个文件用来给中文分割断句
