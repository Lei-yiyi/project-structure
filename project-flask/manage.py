#!/usr/bin/python3
"""
入口
"""
from app import app  # 从模块 app/__init__.py 中导入变量 app，他是 Flask 应用程序实例

from app.views import home
from app.views import users
from app.views import todos

app.register_blueprint(users.blueprint)  # 在 Flask 实例中注册蓝图 users
app.register_blueprint(todos.blueprint)  # 在 Flask 实例中注册蓝图 todos

app.run()
