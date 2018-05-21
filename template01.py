#encoding: utf-8

from flask import Flask,render_template,request,g,url_for,redirect,session
from utlls import login_log
from exts import db
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# with app.app_context():
#     db.create_all()

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
            session['username'] = 'dddoubao'
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

@app.route('/edit/')
def edit():
    if hasattr(g,'username'):
        return '修改成功'
    else:
        return url_for('login')

@app.before_request
def my_before_request():
    if session.get('username'):
        g.username = session.get('username')




if __name__ == '__main__':
    app.run()