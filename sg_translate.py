# -*- coding: utf-8 -*-

from sogou_translate import SogouTranslate, SogouLanguages

PID = '我的pid'
Key = '我的key'
trans = SogouTranslate(PID, Key)

# 中文：ZH_CHS，日语：JA，韩语：KO，英语：EN
# 全部大写


def sg_zh_to_ja(content):
    a1 = trans.translate(content, from_language=SogouLanguages.ZH_CHS, to_language=SogouLanguages.JA)
    return a1


def sg_zh_to_ko(content):
    a2 = trans.translate(content, from_language=SogouLanguages.ZH_CHS, to_language=SogouLanguages.KO)
    return a2


def sg_zh_to_en(content):
    a3 = trans.translate(content, from_language=SogouLanguages.ZH_CHS, to_language=SogouLanguages.EN)
    return a3


def sg_ja_to_zh(content):
    a4 = trans.translate(content, from_language=SogouLanguages.JA, to_language=SogouLanguages.ZH_CHS)
    return a4


def sg_ko_to_zh(content):
    a5 = trans.translate(content, from_language=SogouLanguages.KO, to_language=SogouLanguages.ZH_CHS)
    return a5


def sg_en_to_zh(content):
    a6 = trans.translate(content, from_language=SogouLanguages.EN, to_language=SogouLanguages.ZH_CHS)
    return a6
