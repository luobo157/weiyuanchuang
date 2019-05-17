#暂存，还未封装成函数

from urllib import request, parse
import json

Inp = input("请输入要翻译的内容，输入空格退出")
while Inp != ' ':
    req_url = 'http://fanyi.youdao.com/translate'
    Form_Date = {}
    Form_Date['i'] = Inp
    Form_Date['doctype'] = 'json'
    Form_Date['form'] = 'zh'  #中文：zh
    Form_Date['to'] = 'ko'    #日语：ja，中文zh,英语en
    Form_Date['smartresult'] = 'dict'
    Form_Date['client'] = 'fanyideskweb'
    Form_Date['salt'] = '1526995097962'
    Form_Date['sign'] = '8e4c4765b52229e1f3ad2e633af89c76'
    Form_Date['version'] = '2.1'
    Form_Date['keyform'] = 'fanyi.web'
    Form_Date['action'] = 'FY_BY_REALTIME'
    Form_Date['typoResult'] = 'false'

    data = parse.urlencode(Form_Date).encode('utf-8')
    response = request.urlopen(req_url, data)
    html = response.read().decode('utf-8')

    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print(translate_results)
    Inp = input("请输入要翻译的内容，输入空格退出")
else:
    exit
