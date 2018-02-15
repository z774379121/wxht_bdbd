# 基于werobot，flask的微信公众号后台
微信公众号：少年张君宝

![此处输入图片的描述][1]

---
![此处输入图片的描述][2]
![此处输入图片的描述][3]

## 主要功能

- - [x] 签到功能
- - [x] 训练文章分类获取
- - [x] 记录训练重量
- - [x] 常用数据计算
- - [x] 点歌
- - [x] HTML5游戏支持
- - [x] 聊天功能

---

# **开始**

## 你需要准备的

【appid，appsercet】
没有微信公众号的可以在[微信公众号平台][4]申请一个
也可以直接申请一个测试号开放所有权限（推荐）

一个服务器和80端口的域名

一个机器人tokenid


## 你需要做的


服务器安装redis，mysql（可选）


基本配置：


在公众号平台IP白名单添加上你的服务器IP，设置token并且在config中设置相同的token


数据库初始化：

into Python shell

    >>> from main.models import db
    >>> db.create_all()

**运行**

    python wxht_bdbd.py --host=0.0.0.0 --port=80

**部署**

using gunicorn

    pip install gunicorn

run

    gunicorn -w 3 run:app -p wechat.pid -b 0.0.0.0:80 -D --log-level warning --error-logfile gunicorn-error.log

reload

    kill -HUP `cat wechat.pid`


  [1]: http://oyvgzaycw.bkt.clouddn.com/qrcode_for_gh_11e9b0330a02_258.jpg
  [2]: http://oyvgzaycw.bkt.clouddn.com/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180215100450.png?imageMogr2/thumbnail/!50p
  [3]: http://oyvgzaycw.bkt.clouddn.com/collage.jpg
  [4]: https://mp.weixin.qq.com
