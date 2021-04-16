"""
视图函数
"""
from .. import app

from ..models import db

from flask import render_template, session


"""页面 / 的视图函数"""


@app.route('/')
def index():  # 设置网站的首页面 / 的处理函数为 index
    hasLogin = session.get('hasLogin')  # 该函数首先查询 Session 中的变量 hasLogin
    if hasLogin:  # 如果为真，表示用户已经登录，显示用户已经输入的待做事项和完成事项
        userId = session.get('userId')  # 查询 Session 中的变量 userId，该变量表示已经登录用户的 Id
        items = db.getTodos(userId)  # 获取数据库该用户记录的待做事项
        todos = [item for item in items if item.status == 'todo']  # 获取待做事项中 status 等于 ‘todo’ 的待做事项，保存在列表 todos 中
        dones = [item for item in items if item.status == 'done']  # 获取待做事项中 status 等于 ‘done’ 的待做事项，保存在列表 dones 中
    else:  # 如果为假，表示用户没有登录，显示待做事项和完成事项为空
        items = []
        todos = []
        dones = []
    return render_template('index.html', hasLogin=hasLogin, todos=todos, dones=dones)  # 渲染首页模板 index.html，传递 3 个参数
