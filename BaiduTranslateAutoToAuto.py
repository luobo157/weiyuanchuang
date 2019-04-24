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
