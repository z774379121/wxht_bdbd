#!/usr/bin/python
# coding=utf-8


# import re
from main import app
import random
# from .models import set_user_info
# from .utlis import AESCipher, init_wechat_sdk
# from .plugins.state import set_user_state, get_user_state, \
#     set_user_last_interact_time, get_user_last_interact_time
#from .plugins import tuling


#
# def play_music():
#     """随机音乐"""
#     music.get_douban_fm.delay(openid)
#     return 'success'
#
#
# def developing():
#     """维护公告"""
#     return wechat.response_text('该功能维护中')

# def html5_games():
#     """HTML5游戏"""
#     content = app.config['HTML5_GAMES_TEXT'] + app.config['HELP_TEXT']
#     return wechat.response_text(content)


#
# def command_not_found():
#     """非关键词回复"""
#     # 客服接口回复信息
#     content = app.config['COMMAND_NOT_FOUND_TEXT'] + app.config['HELP_TEXT']
#     wechat_custom.send_text(openid, content)
#     # 转发消息到微信多客服系统
#     return wechat.group_transfer_message()

def random_pic():
    #获得随机图片
    return random.choice(app.config['PIC_URL'])


def command_text():
    #回复指令
    return app.config['COMMAND_TEXT']


def not_time():
    #不是签到时间
    return app.config['NOT_SIGN_TIME_TEXT']


def baidu_food():
    #回复百度网盘
    return app.config['BAIDU_FOOD']


def get_big():
    #恢复增肌列表指令
    return app.config['GET_BIG']


def contact_us():
    #回复投稿
    return app.config['CONTACT_US_TEXT']


def get_weight():
    #回复重量录入格式
    return app.config['GET_WEIGHT']


def html5_game():
    #html5游戏
    return app.config['HTML5_GAMES_TEXT']


def body_look():
    #体态图文
    return [
        [
            "体态拉伸大全(上半身)",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/0.jpg",
            "http://mp.weixin.qq.com/s/rqWuRv5Y7Ffzqrrqba1J8w"
        ],
        [
            "体态拉伸大全(下半身)",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/8GSGCT6TQtuZS_8Qk5hdOg"
        ],
        [
            "力量训练纠正圆肩驼背",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/0c-mG8KzIGYogfBUD5tylA"
        ],
        [
            "骨盆前倾纠正",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/R9Ccz29jXOraDAuTbBDDzA"
        ],
        [
            "体态问题带来的腰疼",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/mlVN2V89c4xAM2qQbEL7KQ"
        ],
        [
            "O型腿",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/Kgj3KbnVBv6RJ-wTRQgawA"
        ],
        [
            "圆肩最简疗法(原创)",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/1EuVcXyzp5NtzOqlYP9HtA"
        ]
    ]


def women_breech():
    #回复女士练臀
    return [
        [
            "翘臀全攻略",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/cda11ce4gw1eys5nwp662j218g0xcgrk.jpg",
            "http://mp.weixin.qq.com/s/9PiH7XhH3Lt4gnHhwbMBGg"
        ],
        [
            "箭步蹲练臀的正确姿势",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/LfTu7IqDe53YZqBgRzWxrA"
        ],
        [
            "不同臀型不同训练方法",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/Xi_QIIAv2ZQheOj5uvxjPA"
        ],
        [
            "还是臀",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/UVQurrUcEYzHuZMdI3esQA"
        ],
        [
            "臀部动作动态图",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/jISXrGmMJSO_ZXO3M_SU4w"
        ],
        [
            "臀臀臀臀臀",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/c7S33OEmLa5frMyEvd7Lkg"
        ],
        [
            "翘臀美腿一块练",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/MfNu99TAW5KRCj21GSYI-A"
        ]
    ]


def mistakes():
    #回复健身误区
    return [
        [
            "日常训练误区",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/23498059_534304986903328_6814248992751222784_n.jpg",
            "http://mp.weixin.qq.com/s/iGUjEDKDfsIvF5yDcr3Uyg"
        ],
        [
            "常见误区汇总",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/CdhY4r7-mapFZwQFubnlzg"
        ],
        [
            "硬拉5大误区",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/pSXsO_z0R7ixHE5P5hAQKw"
        ]
    ]


def bench_press():
    #回复练胸/卧推
    return [
        [
            "Steve Cook教你练胸",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/Steve-Cook-Twitter-Cropped.jpg",
            "http://mp.weixin.qq.com/s/JG-vkFSxpxpwR9ijF1cLsQ"
        ],
        [
            "胸肌动作大全",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/2Nkh-doj0x3cEM7tK4NUew"
        ],
        [
            "强大你的胸肌",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/0c-mG8KzIGYogfBUD5tylA"
        ],
        [
            "胸肌动作大全",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/2Nkh-doj0x3cEM7tK4NUew"
        ],
        [
            "上胸强化指南",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/nyE0UeGKGRYA_Rm_fr5UmQ"
        ],
        [
            "杠铃卧推指南(原创)",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/RLyHXxfxdwnlB3OUtOOkAw"
        ]
    ]


def dead_lift():
    #回复硬拉
    return [
        [
            "日常训练误区",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/8fd16f9153a1eced4ee009eeafa8a9ac_hd.jpg",
            "http://mp.weixin.qq.com/s/iGUjEDKDfsIvF5yDcr3Uyg"
        ],
        [
            "常见误区汇总",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/CdhY4r7-mapFZwQFubnlzg"
        ],
        [
            "硬拉5大误区",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/pSXsO_z0R7ixHE5P5hAQKw"
        ]
    ]


def squat():
    #回复深蹲
    return [
        [
            "深蹲指南",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/23594204_1102138293256701_9164402135880695808_n.jpg",
            "http://mp.weixin.qq.com/s/CYeqylrSFXj07RNMTuk-Ng"
        ],
        [
            "常见误区汇总",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/CdhY4r7-mapFZwQFubnlzg"
        ],
        [
            "硬拉5大误区",
            "I wrote WeRoBot",
            random_pic(),
            "http://mp.weixin.qq.com/s/pSXsO_z0R7ixHE5P5hAQKw"
        ]
    ]


def sport_supply():
    #回复补给
    return [
        [
            "补剂解惑一锅端",
            "补剂的答疑解惑",
            "http://oyvgzaycw.bkt.clouddn.com/23417266_162291357694986_58474699834785792_n.jpg",
            "http://mp.weixin.qq.com/s/zGgf7Wxmbew5BCefLbmR8A"
        ]
        ]


def workout_video():
    #回复健身视频
    return [
        [
            "视频站",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/b6c00845072bffc657a4ec8aa119825d_hd.jpg",
            "http://amuscle.net/article_list.php?id=89"
        ],
        [
            "Steve Cook教你练胸",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/Steve-Cook-Twitter-Cropped.jpg",
            "http://mp.weixin.qq.com/s/JG-vkFSxpxpwR9ijF1cLsQ"
        ]
    ]


def big_arm():
    #回复手臂训练
    return [
        [
            "你要的麒麟臂",
            "description",
            "http://oyvgzaycw.bkt.clouddn.com/maxresdefault.jpg",
            "http://mp.weixin.qq.com/s/Dfo83jZNH-Q2gHWOnlZ8HQ"
        ]
        ]


def big_shoulder():
    #回复肩膀训练
    return [
        [
            "练肩有他就够了",
            "球形三角肌其实很简单",
            "http://oyvgzaycw.bkt.clouddn.com/4_161206112833_2.jpg",
            "http://mp.weixin.qq.com/s/EHqzYPyCSaaqsXnb4KVFhg"
        ]
        ]


def big_back():
    #回复背部训练
    return [
        [
            "倒三角是这样炼成的",
            "想要郭达的背吗",
            "http://oyvgzaycw.bkt.clouddn.com/images.jpg",
            "http://mp.weixin.qq.com/s/T8tdgOCpci87ciO_nqex9A"
        ]
        ]


def figuer_nums():
    #回复计算小工具
    return [
        [
            "1RM重量计算",
            "认清自己的实力，是成功的第一步",
            "http://oyvgzaycw.bkt.clouddn.com/23498821_1911440002505746_3982309632654704640_n.jpg",
            "http://serialdater.net/1rm-calculator/"
        ],
        [
            "热量摄入计算与建议",
            "I wrote WeRoBot",
            random_pic(),
            "http://serialdater.net/tdee-calculator/"
        ],
        [
            "要吃多少蛋白质才够？",
            "I wrote WeRoBot",
            random_pic(),
            "http://serialdater.net/macronutrient-calculator/"
        ]
    ]

