#!/usr/bin/python
# coding=utf-8

from main import app
from werobot.contrib.flask import make_view
from manage import robot

app.add_url_rule(rule='/hello', # WeRoBot 的绑定地址
                endpoint='werobot', # Flask 的 endpoint
                view_func=make_view(robot),
                methods=['GET', 'POST'])


if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run()
