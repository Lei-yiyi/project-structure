"""
数据库访问
"""
from .. import app

from flask_sqlalchemy import SQLAlchemy


user = 'root'  # 数据库的用户名
password = '123456'  # 数据库的密码
database = 'todoDB'  # 数据库的名称
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)  # 数据库访问的 URI
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
orm = SQLAlchemy(app)


"""1. 映射表 users 和表 todos"""


# 使用类 User 映射数据库中的表 users，该表包含 3 个字段 userId、name、password，与类 User 中相同名称的 3 个属性一一对应。
class User(orm.Model):
    __tablename__ = 'users'
    userId = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String(255))
    password = orm.Column(orm.String(255))


# 使用类 Todo 映射数据库中的表 todos，该表包含 4 个字段 todoId、userId、status、title，与类 Todo 中相同名称的 4 个属性一一对应。
class Todo(orm.Model):
    __tablename__ = 'todos'
    todoId = orm.Column(orm.Integer, primary_key=True)
    userId = orm.Column(orm.Integer)
    status = orm.Column(orm.String(255))
    title = orm.Column(orm.String(255))


"""2. 对表 users 进行操作"""


# 函数 login 在表 users 中查找与 name、password 匹配的用户，如果存在，则表示登录成功。
def login(name, password):
    users = User.query.filter_by(name=name, password=password)
    user = users.first()
    return user


# 函数 register 根据 name、password 创建一个新的用户，然后插入到表 users 中。
def register(name, password):
    user = User(name=name, password=password)
    orm.session.add(user)
    orm.session.commit()
    return True


"""3. 对表 todos 进行操作"""


# 函数 getTodos(userId) 在表中查询属于指定用户的待做事项。
def getTodos(userId):
    todos = Todo.query.filter_by(userId=userId)
    return todos


# 函数 addTodo(userId, status, title) 根据 userId、status、title 创建一个新的待做事项，然后插入到表 todos 中。
def addTodo(userId, status, title):
    todo = Todo(userId=userId, status=status, title=title)
    orm.session.add(todo)
    orm.session.commit()
    return True


# 函数 updateTodo(todoId，status) 更新待做事项的 status，当用户完成一个待做事项时，需要将待做事项的 status 从 “todo” 更改为 “done”。
def updateTodo(todoId, status):
    todos = Todo.query.filter_by(todoId=todoId)
    todos.update({'status': status})
    orm.session.commit()
    return True


# 函数 deleteTodo(todoId) 删除待做事项。
def deleteTodo(todoId):
    todos = Todo.query.filter_by(todoId=todoId)
    todos.delete()
    orm.session.commit()
    return True
