#!/usr/bin/python
# coding=utf-8

import re
import werobot
import config
from main import app
from main.plugins import tuling, sign, simsimi, music
from main.response import *

#初始化werobot
robot = werobot.WeRoBot(token=app.config['TOKEN'],
                        app_id=app.config['APP_ID'],
                        app_secret=app.config['APP_SECRET'],
                        logger=app.logger)
#初始化聊天机器人
turobot = tuling.TuLing()


def res(msg):
    #机器人回复
    return turobot.get_response(msg)

class Respons:
    '''回复函数'''

    def __init__(self):
        self.body_look = body_look
        self.big_arm = big_arm
        self.big_back = big_back
        self.squat = squat
        self.dead_lift = dead_lift
        self.big_shoulder = big_shoulder
        self.beech_press = bench_press
        self.command_text = command_text
        self.baidu_food = baidu_food
        self.get_big = get_big
        self.contact_us = contact_us
        self.sport_supply = sport_supply
        self.workout_video = workout_video
        self.figuer_nums = figuer_nums
        self.daily_sign = sign.daily_sign
        self.women_breech = women_breech
        self.get_weight = get_weight
        self.html5_game = html5_game

respons = Respons()

#关键字指令
commands = {
    u'^00$|^\?|^？|^帮助': respons.command_text,
    u'^1$': respons.baidu_food,
    u'^2$': respons.figuer_nums,
    u'^3$': respons.workout_video,
    u'^4$': respons.body_look,
    u'^5$': respons.get_weight,
    u'^6$': respons.women_breech,
    u'^7$': respons.get_big,
    u'^71$': respons.beech_press,
    u'^72$': respons.big_shoulder,
    u'^73$': respons.squat,
    u'^74$': respons.big_back,
    u'^75$': respons.big_arm,
    u'701': respons.beech_press,
    u'702': respons.squat,
    u'703': respons.dead_lift,
    u'8': respons.sport_supply,
    u'合作|9': respons.contact_us,
    u'qd': respons.daily_sign,
    u'^音乐|^音樂': 'play_music',
    u'^玩游戏|^游戏|^play': respons.html5_game
}



#订阅信息
@robot.subscribe
def subscribe(message):
    return app.config['WELCOME_TEXT']


@robot.filter(re.compile(u"^点歌"))
def a(message):
    try:
        songnamel = message.content.split(' ')[1:]
        songname = [k.encode('utf-8') for k in songnamel]
        songname = ' '.join(songname)
    except:
        return '点歌是【点歌 歌名】啊 猪'
    songurl = music.get_music(songname)
    return [
        songname,
        "最新力作",
        songurl,
        ]



#重量录入过滤
@robot.filter(re.compile(u"下拉.*?|^卧推|^硬拉|^引体|^俯卧撑|^肩推|^深蹲"))#, re.compile("卧推.*?"), re.compile("硬拉.*?"),  re.compile("引体.*?"), re.compile("俯卧撑.*?"), re.compile("肩推.*?"))
def b(message):
    # 全角空格
    message.content = message.content.replace(u'　', ' ')
    # 清除行首空格
    message.content = message.content.lstrip()
    klist = message.content.split(' ')
    m = {
        u'^卧推': 'benchpress',
        u'^硬拉': 'deadlift',
        u'^深蹲': 'squat',
        u'^引体|^引体向上': 'ytxs',
        u'^俯卧撑': 'fwc',
        u'^下拉|^高位下拉': 'gwxl',
        u'^肩推|^推肩|^肩举': 'shoulderpress'

    }
    u = simsimi.get_user_info(message.source)
    if u:
        kdict = {
            'benchpress': u[0].benchpress,
            'deadlift': u[0].deadlift,
            'squat': u[0].squat,
            'ytxs': u[0].ytxs,
            'fwc': u[0].fwc,
            'gwxl': u[0].gwxl,
            'shoulderpress': u[0].shoulderpress
        }
    else:
        kdict = {
            'benchpress': 0,
            'deadlift': 0,
            'squat': 0,
            'ytxs': 0,
            'fwc': 0,
            'gwxl': 0,
            'shoulderpress': 0
        }
    for i in klist:
        for key_word in m:
            if re.match(key_word, i):
                try:
                    k = int(filter(str.isdigit, i.encode('utf-8')))
                    if k > 999:
                        return '你别唬我哦\t这么多？'
                except:
                    return '数据错误，请检查格式\n回复【5】查看详情'
                kdict[m[key_word]] = k
    return simsimi.check_in(message.source, kdict['benchpress'], kdict['deadlift'], kdict['squat'],
    kdict['ytxs'], kdict['fwc'], kdict['gwxl'], kdict['shoulderpress'])


@robot.text
def hello(message):
    #签到
    if message.content.encode('utf-8') in ['qd', '0', '签到']:
        return commands['qd'](message.source)
    for key_word in commands:
        if re.match(key_word, message.content):
            return commands[key_word]()
    # 重量查询
    if message.content == 'xx':
        return simsimi.show_uese_info(message.source)
    elif message.content == 'w':
        return commands[u'明信片'](message.content)
    # 非关键字 tuling处理
    else:
        return res(message.content)


@robot.location
def cpimg(message):
    return [
        [
            "title",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/IMG_0429.JPG.png",
            "http://mp.weixin.qq.com/s/1EuVcXyzp5NtzOqlYP9HtA"
        ],
        [
            "whtsky",
            "I wrote WeRoBot",
            "https://secure.gravatar.com/avatar/0024710771815ef9b74881ab21ba4173?s=420",
            "https://github.com/z774379121/pyblog"
        ]
    ]

# 让服务器监听在 0.0.0.0:80
# robot.config['HOST'] = '0.0.0.0'
# robot.config['PORT'] = 80
# robot.run()