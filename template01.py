#encoding: utf-8

from flask import Flask,render_template,request,g
from flask_sqlalchemy import SQLAlchemy
from utlls import login_log
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    # print request.args
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'dddoubao' and password =='111':
            g.username = 'dddoubao'
            login_log()
            return '恭喜你，登录成功'
        else:
            return '您输入的用户名或者密码不对'

        print '用户名：',username
        print '密码：',password
        return 'post'

@app.route('/list/')
def list():
    return render_template('list.html')


if __name__ == '__main__':
    app.run()