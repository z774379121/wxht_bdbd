#!/usr/bin/python
# coding=utf-8

from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from redis import Redis


app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

handler = RotatingFileHandler('aggg.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.CRITICAL)
app.logger.addHandler(handler)


redis = Redis()