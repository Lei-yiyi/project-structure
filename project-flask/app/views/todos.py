"""
蓝图
"""
from flask import Blueprint

from ..models import db

from flask import request, session, jsonify


blueprint = Blueprint('todos', __name__, url_prefix='/todos')


"""1. 请求 /todos/add 页面"""


# 使用 POST 方法请求 /todos/add 页面用于新增一个待做事项
@blueprint.route('/add', methods=['POST'])
def addTodo():
    userId = session.get('userId')
    status = 'todo'
    title = request.json['title']
    db.addTodo(userId, status, title)  # 调用 db.addTodo(userId, status, title) 向表 todos 中插入一行
    return jsonify({'error': None});  # 在例子中忽略了错误处理，返回错误为 None


"""2. 请求 /todos/update 页面"""


# 当用户完成一个待做事项后，将待做事项移入到完成事项中，需要使用 POST 方法请求 /todos/update 页面用于更新待做事项的 status
@blueprint.route('/update', methods=['POST'])
def updateTodo():
    todoId = request.json['todoId']
    status = 'done'
    db.updateTodo(todoId, status)  # 调用 db.updateTodo(todoId, status) 个更新待做事项的 status
    return jsonify({'error': None});


"""3. 请求 /todos/delete 页面"""


# 使用 POST 方法请求 /todos/delete 页面用于删除一个待做事项
@blueprint.route('/delete', methods=['POST'])
def deleteTodo():
    todoId = request.json['todoId']
    db.deleteTodo(todoId)  # 调用 db.deleteTodo(todoId) 删除指定的待做事项
    return jsonify({'error': None});
