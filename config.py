#!/usr/bin/python
# coding=utf-8


DEBUG = False

TULING_URL = 'http://www.tuling123.com/openapi/api'
MAIN_URL = 'http://jjweix.qmvu.me/help'
WELCOME_TEXT = u'感谢关注本公众号[愉快]\n我是助手胖虎[调皮]\n回复数字【00】或者【帮助】打开新世界的大门\n'

COMMAND_TEXT = u'回复关键词查看\n【0】签到  /拥抱/拥抱/拥抱\n【1】获取模块化饮食表\n【2】计算器\n\
【3】训练视频\n【4】体态纠正与塑性\n【5】记录重量  /奋斗/奋斗/奋斗\n【6】女士专场\n【7】\n /篮球 瘦人增肌 /篮球\n         and\n /足球 胖人减脂 /足球\n【8】有关补剂\n【9】合作与投稿\n\
-------------------------------\n新加点歌功能|格式:点歌 歌名\n如 点歌 红豆\n点歌 BEAT IT\n赶紧试试吧'

GET_BIG = u'【71】胸\n【72】肩\n【73】腿\n【74】背\n【75】手臂\n\
-------------------------------\n\
-------------三大项-----------\n\
-------------------------------\n【701】卧推\n【702】深蹲\n【703】硬拉'

BAIDU_FOOD = u'链接: https://pan.baidu.com/s/1mj4VL4s 密码: 8nvg \n\
-------------------------------\n图片分辨率6224*7998 \n\
-------------------------------\n大图请在电脑中查看\n-------------------------------\n建议搭配数字【2】使用'

GET_WEIGHT = u'请按以下格式录入你的重量\n动作重量空格动作重量,如下\n\
-------------------------------\n深蹲100 卧推80 引体10\n硬拉150\n\
-------------------------------\n仅支持 【深蹲】 【卧推】\n【硬拉】 \
【引体】 【下拉】\n【肩推】 【俯卧撑】 \n重量是做一下的重量(kg)\n俯卧撑，引体记录的是个数\n\
如果不清楚自己做一下的重量请先回复【2】进行计算\n支持只输入需要记录的动作\n没输入的动作默认为上次的数据没有则为0\n录入频率最高每天一次，建议一周一录 科学合理 方便查看'

COMMAND_NOT_FOUND_TEXT = u"收到你的留言啦！"

CANCEL_COMMAND_TEXT = u"已回到正常模式啦啦啦~\n\n"

HELP_TEXT = u"\n\n回复 “ ? ” 查看主菜单"

BBS_URL_TXT = u'<a href="http://wsq.discuz.qq.com/?siteid=264557099">进入论坛：点击这里</a>'

HTML5_GAMES_TEXT = u'<a href="http://www.html5tricks.com/demo/wuziqi/index.html">开始玩游戏：\
点击这里  五子棋</a>\n<a href="http://h.5qwan.com/games/bunengsi/">开始玩游戏：\
点击这里  跑酷</a>\n<a href="http://gopherwoodstudios.com/sandtrap/sand-trap.htm">开始玩游戏：点击这里 倒沙子</a>'

NOT_SIGN_TIME_TEXT = u"离起床还早呢~\n快睡觉吧~\n\n签到时间从早上6点开始\n\n记得每天签到啦~"

CONTACT_US_TEXT = u"我们欢迎各类型的合作和投稿\n\n请联系：zjj19950716@gmail.com\n微信，QQ：774379121"

PIC_URL = ['http://oyvgzaycw.bkt.clouddn.com/23348195_277075476148339_52120424569372672_n.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/IMG_0691.JPG',
           'http://oyvgzaycw.bkt.clouddn.com/deadlift.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/Koala.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/squart.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/v2-1c1c19c458d01ca8341a68ff9713c7b3_hd.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/v2-7bff0c2bda43f5a080de20c650e7d2e9_hd.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/v2-f2e609b2fc5c45639c25f6b9d9387114_hd.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/%E5%BD%AD%E4%BA%8E%E6%99%8F.JPG',
           'http://oyvgzaycw.bkt.clouddn.com/%E6%B0%B4%E8%9C%9C%E8%87%80.jpg',
           'http://oyvgzaycw.bkt.clouddn.com/%E9%A5%AE%E9%A3%9F.jpg',
           'http://n.sinaimg.cn/translate/w1080h1080/20180201/NtEp-fyrcsrw6393039.jpg',
           'http://n.sinaimg.cn/translate/w1080h1080/20180201/pW-x-fyrcsrw6393712.jpg',
           'http://n.sinaimg.cn/translate/w779h810/20180201/ADx6-fyrcsrw6395328.jpg',
           'http://n.sinaimg.cn/translate/w640h640/20180201/puqp-fyrcsrw6395457.jpg',
           'http://n.sinaimg.cn/translate/w600h600/20180201/PFCO-fyrcsrw6395229.jpg',
           'http://n.sinaimg.cn/translate/w702h855/20180201/jHLD-fyrcsrw6395181.jpg',
           'http://n.sinaimg.cn/translate/w700h834/20180201/I8_J-fyrcsrw6395096.jpg',
           'http://n.sinaimg.cn/translate/w669h669/20180201/qqxc-fyrcsrw6394978.jpg',
           'http://n.sinaimg.cn/translate/w1080h1099/20180201/1Bzy-fyrcsrw6394835.jpg',
           'http://n.sinaimg.cn/translate/w1080h1310/20180201/njVs-fyrcsrw6394756.jpg',
           'http://n.sinaimg.cn/translate/w577h577/20180201/MQvf-fyrcsrw6394469.jpg',
           'http://n.sinaimg.cn/translate/w700h798/20180201/2wLt-fyrcsrw6395575.jpg'
           ]

