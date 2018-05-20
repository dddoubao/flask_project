#encoding: utf-8

from flask import g


def login_log():
    print u'当前用户是:%s' % g.username