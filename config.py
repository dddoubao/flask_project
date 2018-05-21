#encoding: utf-8
from flask import session
import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'
USERNAME = 'root'
PASSWORD = '2200684'


DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)