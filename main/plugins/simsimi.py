#!/usr/bin/python
# coding=utf-8

import time
from datetime import datetime
from main import redis
from ..models import get_user_info, save_user_info


# 数据录入
def check_in(openid, benchpress,deadlift,squat,
             ytxs,fwc,gwxl,shoulderpress):
    current_milli_time = int(round(time.time() * 1000))
    current_hour = int(datetime.fromtimestamp(
        current_milli_time / 1000).strftime('%H'))

    if current_hour < 6:
        return '机器人还没起床，请于6点后录入'
    else:
        user_info = get_user_info(openid)
        # 读取上次签到时间戳
        if user_info:
            last_reg_time = long(time.mktime(user_info[0].regtime.timetuple()) * 1000.0 + user_info[0].regtime.microsecond / 1000.0)
        else:
            last_reg_time = current_milli_time-864000000
        # 今日凌晨的时间戳
        today_dt = datetime.fromtimestamp(
            current_milli_time / 1000).strftime('%Y-%m-%d')
        today_timestamp = int(round(time.mktime(
            datetime.strptime(today_dt, '%Y-%m-%d').timetuple()) * 1000))
        # 上次签到时间大于今日凌晨的时间戳，今日已经签到过
        if last_reg_time >= today_timestamp:
            # 返回签到信息
            return '今天已经记录过了 请不要重复记录\n回复【xx】查看记录'
        else:
            save_user_info(openid, benchpress, deadlift, squat,
             ytxs, fwc, gwxl, shoulderpress)
            return '录入成功\n回复【xx】查看近期记录'


# 显示用户数据
def show_uese_info(openid):
    if redis.get('mark'):
        mark = int(redis.get('mark'))
        redis.set('mark', int(redis.get('mark'))+1, 30)
    else:
        mark = 0
        redis.set('mark', 1, 30)
    user_info = get_user_info(openid, n=mark)
    if user_info:
        m = ['%s \n卧推->%03dkg 硬拉->%03dkg\n深蹲->%03dkg 引体->%03d个\n俯卧撑->%03d个 肩推->%03dkg\n高位下拉->%03dkg\n-------------------------------' % (u.regtime.strftime("%Y-%m-%d"), u.benchpress, u.deadlift, u.squat, u.ytxs, u.fwc, u.shoulderpress, u.gwxl)
             for u in user_info]
        m.append('30秒继续回复xx 查看更早5条')
    else:
        m = ['没有发现数据', '请核实', '或者等待30S重试']
    return '\n'.join(m)
