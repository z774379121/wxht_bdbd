#!/usr/bin/python
# coding=utf-8

import os


DEBUG = True

HOST_URL = ""
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
 							'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'datas.sqlite')
APP_ID = ''
APP_SECRET = ''
TOKEN = ''
EncodingAESKey = ''

TULING_KEY = ''