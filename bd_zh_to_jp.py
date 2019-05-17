# -*- coding: utf-8 -*-

import requests
import time
import hashlib
import json

appid = "20181130000241491"
baidukey = "hRIiKPZLQyZAsfuabRCz"
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = appid
cyber = baidukey

def bd_zh_to_jp(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'zh',
        'to': 'jp',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'zh' + '&to=' + 'jp' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']

def bd_jp_to_zh(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'jp',
        'to': 'zh',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'jp' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']
