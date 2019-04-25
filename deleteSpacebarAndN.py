#coding:utf8
#注意：由于未限制文件类型，此程序可以替换path值文件夹下所有文件，包括py文件里面的内容
#此程序只是替换掉了多余的换行，删除了多余的空格

import os


def reset():
    i = 0
    path = r".\article\\" #当前文件夹下article文件夹里的内容
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        filePath = path + filename + filetype
        # 此处写入需要替换的代码，空格" ",两个空格"  ",空字符"",换行符号"\n",全角空格"\u3000"多被用来执行首行缩进，tab制表符"\t"
        # 1.把所有空格替换成空字符
        # 2.把所有换行符替换成空格
        # 3.把两个空格替换成一个空格，多执行几次，就只剩下一个空格了
        # 4.然后把空格替换成换行符号
        alter(filePath, " ", "")
        alter(filePath, "\u3000", "")
        alter(filePath, "\n", " ")
        alter(filePath, "  ", " ")
        alter(filePath, "  ", " ")
        alter(filePath, "  ", " ")
        alter(filePath, " ", "\n")

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
    
reset()
