# -*- coding: utf-8 -*-

import requests
import time
import hashlib
import json

appid = "我的appid"
baidukey = "我的key"
api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = appid
cyber = baidukey

def bd_auto_to_jp(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'auto',
        'to': 'jp',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'auto' + '&to=' + 'jp' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']

def bd_auto_to_zh(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'auto',
        'to': 'zh',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'auto' + '&to=' + 'zh' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']

def bd_auto_to_kor(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'auto',
        'to': 'kor',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'auto' + '&to=' + 'kor' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']

def bd_auto_to_en(word):
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    paramas = {
        'q': word,
        'from': 'auto',
        'to': 'en',
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'auto' + '&to=' + 'en' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']
