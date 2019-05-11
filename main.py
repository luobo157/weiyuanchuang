# 处理文件的引用
import os
# 分段的引用
import linecache
# 必应翻译的引用
import urllib.request
import urllib.parse

def bingTranslateAutoToJa(content, _from_, _to_):
    """ 自动:auto, 中文:zh, 英文:en, 日语：ja"""
    if (_from_ == 'auto'):
        _from_ = ''
    if (_to_ == 'auto'):
        _to_ = 'ja'
        # _to_ = 'zh' if content[0] < chr(127) else 'en'
    data = {}
    data['from'] = '"' + _from_ + '"'
    data['to'] = '"' + _to_ + '"'
    data['texts'] = '["'
    data['texts'] += content
    data['texts'] += '"]'
    data['options'] = "{}"
    data['oncomplete'] = 'onComplete_3'
    data['onerror'] = 'onError_3'
    data['_'] = '1430745999189'
    data = urllib.parse.urlencode(data).encode('utf-8')
    strUrl = "http://api.microsofttranslator.com/v2/ajax.svc/TranslateArray2?" + data.decode() + "&appId=%223DAEE5B978BA031557E739EE1E2A68CB1FAD5909%22"

    response = urllib.request.urlopen(strUrl)
    str_data = response.read().decode('utf-8')
    tmp, str_data = str_data.split('"TranslatedText":')
    translate_data = str_data[1:str_data.find('"', 1)]
    return translate_data



# 获取当前文件夹中所有记事本txt文件清单，分段翻译
fns = (fn for fn in os.listdir() if fn.endswith('.txt'))
for fn in fns:
    with open(fn, encoding='utf8') as fp:
        hang = 1    #初始行数设为0
        num_lines = sum(1 for line in open(fn,'rb'))    #文章的实际行数
        while hang < num_lines:
            a1 = str(linecache.getline(fn, hang))
            a1 = a1.replace('\n', '')
            a1 = bingTranslateAutoToJa(a1, 'auto', 'auto')
            print(a1)
            with open('t.txt', 'a+', encoding='utf8') as fp2:
                fp2.write(a1 + '\n')
            hang = hang + 1
    os.remove(fn)
    os.rename('t.txt', fn)
