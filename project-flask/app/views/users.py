"""
蓝图
"""
from flask import Blueprint

from ..models import db

from flask import render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


# 导入相关模块，然后创建蓝图对象 blueprint，参数 ‘users’ 是蓝图的名称，参数 url_prefix 是页面的前缀。
# 蓝图 users 包含有 3 个页面 /users/login、/users/register、/users/logout，设置 url_prefix 为 /users 后，
# 使用 @app.route 注册页面的处理函数时，使用 /login、/register、/logout 作为 URL 即可，省略了前缀 /users。
blueprint = Blueprint('users', __name__, url_prefix='/users')


"""1. 登录表单"""


# 使用 WTForms 表单实现登录表单，LoginForm 继承于 FlaskForm，它包含 2 个字段 name 和 password。
class LoginForm(FlaskForm):
    name = StringField(
        label='姓名',
        validators=[
            DataRequired(message='姓名不能为空')
        ]
    )  # name 字段的验证器 DataRequired 要求字段不能为空

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )  # password 字段的验证器 DataRequired 要求字段不能为空，验证器 Length 要求密码至少包括 3 个字符

    submit = SubmitField('登录')


"""2. 请求 /users/login 页面"""


# 页面 /users/login 有两种请求方法：GET 和 POST。
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # 使用 GET 方法请求页面 /users/login 时，用于显示登陆界面
        form = LoginForm()
        return render_template('login.html', form=form)  # 使用 render_template 渲染登陆页面模板 login.html
    else:  # 使用 POST 方法请求页面 /users/login 时，用于向服务器提交登陆请求
        form = LoginForm()  # 创建一个 LoginForm 实例
        if form.validate_on_submit():  # 调用 form.validate_on_submit() 验证表单中的字段是否合法
            name = form.name.data
            password = form.password.data
            user = db.login(name, password)  # 调用 db.login(name, password) 在数据库验证用户身份，如果登录成功，则返回登录的用户 user
            if user:  # 如果登录成功
                session['hasLogin'] = True  # 在 Session 中设置 hasLogin 为 True
                session['userId'] = user.userId  # 在 Session 中设置 userId 为登录用户的 userId
                return redirect('/')  # 调用 redirect(’/’)，用户登录成功后，浏览器重定向到网站根页面
        return render_template('login.html', form=form)


"""3. 注册表单"""


class RegisterForm(FlaskForm):
    name = StringField(
        label='姓名',
        validators=[
            DataRequired(message='姓名不能为空')
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=3, message='密码至少包括 3 个字符')
        ]
    )

    submit = SubmitField('注册')


"""4. 请求 /users/register 页面"""


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)
    else:
        form = RegisterForm()
        if form.validate_on_submit():
            name = form.name.data
            password = form.password.data
            if db.register(name, password):
                return redirect('/')
        return render_template('register.html', form=form)


"""5. 退出系统"""


# 访问 /users/logout 页面时，用户退出系统。
@blueprint.route('/logout')
def logout():
    session['hasLogin'] = False
    return redirect('/')
