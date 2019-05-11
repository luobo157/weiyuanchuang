PID = '搜狗PID'
Key = '搜狗Key'

from sogou_translate import SogouTranslate, SogouLanguages

trans = SogouTranslate(PID, Key)

en_text = 'Hello, world!'
zh_text = trans.translate(en_text, from_language=SogouLanguages.EN, to_language=SogouLanguages.ZH_CHS)
print(zh_text) # '你好，世界！'
