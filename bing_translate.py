#本文件为封装的函数，使用方法为a1 = bingTranslateAutoToAuto（content, _from_, _to_）
#content为string类型的utf8编码的数据

# 必应翻译的引用
import urllib.request
import urllib.parse

def bing_auto_to_ja(content, _from_, _to_):
    """ 自动:auto, 中文:zh, 英文:en, 日语：ja，韩语：ko"""
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

def bing_auto_to_zh(content, _from_, _to_):
    """ 自动:auto, 中文:zh, 英文:en, 日语：ja，韩语：ko"""
    if (_from_ == 'auto'):
        _from_ = ''
    if (_to_ == 'auto'):
        _to_ = 'zh'
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

def bing_auto_to_ko(content, _from_, _to_):
    """ 自动:auto, 中文:zh, 英文:en, 日语：ja，韩语：ko"""
    if (_from_ == 'auto'):
        _from_ = ''
    if (_to_ == 'auto'):
        _to_ = 'ko'
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

def bing_auto_to_en(content, _from_, _to_):
    """ 自动:auto, 中文:zh, 英文:en, 日语：ja，韩语：ko"""
    if (_from_ == 'auto'):
        _from_ = ''
    if (_to_ == 'auto'):
        _to_ = 'en'
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
