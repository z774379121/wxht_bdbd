#!/usr/bin/python
# coding=utf-8

import re
import json
import time
import random
import requests
import urllib
import pprint


def get_song_mid(parme):
    uencode = repr(parme).replace('\\x', '%')
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    r = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=%s&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'%(int(random.random() * 2147483647) * int(time.time() * 1000) % 10000000000, uencode), headers=headers)
    c = r.content
    c = c.rstrip(')')
    c = c.lstrip('callback(')
    c = eval(c)
    try:
        return c['data']['song']['list'][0]['grp'][0]['file']['media_mid']
    except:
        return c['data']['song']['list'][0]['file']['media_mid']



def resolve(songmid):
    """
    resolve audio url
    :param url: like 'https://y.qq.com/n/yqq/song/000YU69H3N55rZ.html'
    :return:
    """
    # filename = 'C400' + songmid + '.m4a'
    # guid = int(random.random() * 2147483647) * int(time.time() * 1000) % 10000000000
    #
    # d = {
    #     'format': 'json',
    #     'cid': 205361747,
    #     'uin': 0,
    #     'songmid': songmid,
    #     'filename': filename,
    #     'guid': guid,
    # }
    # r = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg', params=d, verify=False)
    # vkey = json.loads(r.content)['data']['items'][0]['vkey']
    # audio_url = 'http://dl.stream.qqmusic.qq.com/%s?vkey=%s&guid=%s&uin=0&fromtag=66' % (filename, vkey, guid)
    audio_url = 'http://isure.stream.qqmusic.qq.com/C100%s.m4a?fromtag=32'%songmid
    return audio_url


# print resolve('https://y.qq.com/n/yqq/song/000YU69H3N55rZ.html')
def get_music(songname):
    try:
        audiourl = 'http://isure.stream.qqmusic.qq.com/C100{0}.m4a?fromtag=32'.format(get_song_mid(songname))
        return audiourl
    except:
        return 'http://isure.stream.qqmusic.qq.com/C100001U8CD42CFacZ.m4a?fromtag=32'





