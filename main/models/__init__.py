#!/usr/bin/python
# coding=utf-8

import time
from .. import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from .sign import Sign
from .user import User



def get_user_info(openid, n=0):
    user_info = User.query.filter_by(openid=openid).order_by(User.regtime.desc()).limit(5).offset(5*n).all()
    return user_info


def save_user_info(openid, benchpress, deadlift, squat,
             ytxs, fwc, gwxl, shoulderpress):
    # 写入数据库
    user_info = User(openid, benchpress, deadlift, squat,
            ytxs, fwc, gwxl, shoulderpress)
    user_info.save()
    return None


def get_sign_info(openid):
    """读取签到信息"""
    sign_info = Sign.query.filter_by(openid=openid).first()
    if not sign_info:
        return {
            "lastsigntime": 0,
            "keepdays": 0,
            "totaldays": 0
        }
    else:
        return {
            "lastsigntime": int(sign_info.lastsigntime),
            "keepdays": int(sign_info.keepdays),
            "totaldays": int(sign_info.totaldays)
        }


def update_sign_info(openid, lastsigntime, totaldays, keepdays):
    """更新签到信息"""
    # 写入数据库
    sign_info = Sign.query.filter_by(openid=openid).first()
    if not sign_info:
        sign_info = Sign(openid, lastsigntime, totaldays, keepdays)
        sign_info.save()
    else:
        sign_info.lastsigntime = lastsigntime
        sign_info.totaldays = totaldays
        sign_info.keepdays = keepdays
        sign_info.update()

    return None


def get_today_sign_ranklist(today_timestamp):
    """获取今日签到排行榜"""
    data = Sign.query.join(User, Sign.openid == User.openid) \
        .add_columns(User.nickname) \
        .filter(Sign.lastsigntime >= today_timestamp) \
        .order_by(Sign.lastsigntime).all()

    return data


def get_sign_keepdays_ranklist(today_timestamp):
    """获取续签排行榜"""
    data = Sign.query.join(User, Sign.openid == User.openid) \
        .add_columns(User.nickname) \
        .filter(Sign.lastsigntime >= today_timestamp) \
        .order_by(Sign.keepdays.desc(),
                  Sign.totaldays.desc(),
                  Sign.lastsigntime).limit(6).all()

    return data