#encoding: utf-8

from flask import Flask,redirect,url_for


app = Flask(__name__)

@app.route('/')
def index():
    login_rul = url_for('login')
    return redirect(login_rul)
    return u'这是您的首页'

@app.route('/login000/')
def login():
    return "这是登录页面121321"

@app.route('/question/<is_login>')
def question(is_login):
    if is_login =="1":
        return "已经登录了，这是问答页面"
    else:
        return redirect(url_for("login"))


if __name__ == '__main__':
    app.run()
