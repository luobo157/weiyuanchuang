# coding: utf8
'''
 @Author: LCY
 @url：https://www.jb51.net/article/145740.htm
 @Contact: lchuanyong@126.com
 @blog: http://http://blog.csdn.net/lcyong_
 @Date: 2018-01-15
 @Time: 19:19
 说明： appid和secretKey为百度翻译文档中自带的，需要切换为自己的
   python2和python3部分库名称更改对应如下：
   httplib  ----> http.client
   md5   ----> hashlib.md5
   urllib.quote ----> urllib.parse.quote
 官方链接：
   http://api.fanyi.baidu.com/api/trans/product/index

'''



#本文件为封装的函数，使用方法为a1 = BaiduTranslateAutoToAuto（content, _from_, _to_）
#content为string类型的utf8编码的数据
#需要添加"我的appid"和"我的key"才可使用


# 百度翻译的引用
import http.client
import hashlib
import json
import urllib
import random

def BaiduTranslateAutoToAuto(content):
    appid = '我的appid' #appid和secretkey都是自己的
    secretKey = '我的key'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'auto'  # 源语言
    toLang = 'auto'  # 翻译后的语言，中文zh，日语jp，英语en
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        print(dst)  # 打印结果
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
