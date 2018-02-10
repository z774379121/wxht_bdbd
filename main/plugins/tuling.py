#!/usr/bin/python
# coding=utf-8

import random
import requests
from main import app

class TuLing:
    def __init__(self):
        self.default_answer = [u'么么哒', u'说啥呢……', u'叫我干嘛', u'我不听我不听', u'=。=']
        self.key = app.config['TULING_KEY']
        self.url = app.config['TULING_URL']


    def bad_word_filter(self, answer):
        for word in ['撸', '微', '胸', '屌', '插', '叼', '操', '草', '舔',
                     '骚', '逼', '淫', '好爽', '鸡巴', '嫖', '干你', '你妈',
                     '你妹', '越大声', '夹紧', '上床', '搜索', '不要停',
                     '淘宝', '扣扣', 'QQ', '.com']:
            if word.decode('UTF-8') in answer:
                return True
        return False



    def get_response(self, msg):
        if self.bad_word_filter(msg):
            return random.choice(self.default_answer)
        KEY = self.key
        URL = self.url
        data = {
            'key': KEY,
            'info': msg,
            'userid': 'wechat-robot'
        }
        try:
            r = requests.post(URL, data=data).json()
            return r.get('text')
        except Exception, e:
            app.logger.warning("simsimi 请求或解析失败: %s, text: %s" % (e, msg))
            return random.choice(self.default_answer)

