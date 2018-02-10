#!/usr/bin/python
# coding=utf-8

import datetime
from . import db

class User(db.Model):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4'
    }

    openid = db.Column(db.String(32), nullable=False)
    benchpress = db.Column(db.SmallInteger, default=0, nullable=False)
    deadlift = db.Column(db.SmallInteger, default=0, nullable=False)
    squat = db.Column(db.SmallInteger, default=0, nullable=False)
    ytxs = db.Column(db.SmallInteger, default=0, nullable=False)
    fwc = db.Column(db.SmallInteger, default=0, nullable=False)
    gwxl = db.Column(db.SmallInteger, default=0, nullable=False)
    shoulderpress = db.Column(db.SmallInteger, default=0, nullable=False)
    regtime = db.Column(db.DateTime, default=datetime.datetime.now, primary_key=True, nullable=False)

    def __init__(self, openid, benchpress=None, deadlift=None,
                 squat=None, ytxs=None,
                 fwc=None, gwxl=None, shoulderpress=None, regtime=None):
        self.openid = openid
        self.benchpress = benchpress
        self.deadlift = deadlift
        self.squat = squat
        self.ytxs = ytxs
        self.fwc = fwc
        self.gwxl = gwxl
        self.shoulderpress = shoulderpress
        self.regtime = regtime

    def __repr__(self):
        return '<openid %r>' % self.openid

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return self

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return self