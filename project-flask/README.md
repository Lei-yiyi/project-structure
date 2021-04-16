# project-flask

## 1. 功能简介
### 功能简介

    使用 Flask 开发一个功能完整的 Web 应用程序 —— 待做清单，该 Web 应用程序记录待做事项。程序提供了用户注册的功能，用户登录后，录入的待做事项被记录在服务端，如果换一台机器，使用浏览器登录后，仍然能够看到已经录入的待做事项。

### 涉及的知识点

     模板
     WTF 表单和表单验证
     蓝图
     ORM 访问数据库
     会话 Session

### 运行程序

     -- 源程序下载
     
     -- 源文件目录
     
        ├── app  -- 项目的主要功能实现  
        │   ├── models              # 数据库模型文件
        │   |   ├── __init__.py
        │   │   ├── db.sql          # 创建数据库的 SQL 脚本文件 
        │   │   └── db.py           # 提供访问数据库的功能函数 
        │   ├── static              # 静态资源文件
        │   │   |── style.css       # 样式文件
        │   │   └── script.js	    # 调用后端服务的接口
        │   ├── templates           # 模板文件
        │   │   ├── index.html	    # 首页的页面模板
        │   │   ├── login.html	    # 登录的页面模板
        │   │   └── register.html   # 注册的页面模板
        │   ├── views               # 视图文件
        │   |   ├── __init__.py
        │   |   ├── home.py         # 实现视图函数
        │   │   ├── users.py        # 实现蓝图 users，提供登录、注册的功能 
        │   │   └── todos.py        # 实现蓝图 todos，提供增加、修改、删除待做事项 todo 的功能
        │   └── __init__.py         # Flask 实例
        ├── manage.py         # 入口
        ├── README.md         # 仓库的说明，比如该项目的介绍等
        └── requirements.txt  # 项目所依赖的第三方包以及版本号，方便在其他位置生成相同的虚拟环境以及依赖
        
        后端实现：
        db.sql	创建数据库的 SQL 脚本文件  
        
        __init__.py	Flask 实例  
        manage.py	入口  
        
        db.py	提供访问数据库的功能函数 
        
        home.py     实现视图函数
        users.py	实现蓝图 users，提供登录、注册的功能  
        todos.py	实现蓝图 todos，提供增加、修改、删除待做事项 todo 的功能 
        
        前端实现：
        index.html	首页的页面模板  
        login.html	登录的页面模板  
        register.html	注册的页面模板  
        
        style.css	样式文件  
        
        script.js	调用后端服务的接口 

     -- 安装相关的库 requirements.txt
     
        pip3 install flask
        pip3 install pymysql
        pip3 install SQLAlchemy
        pip3 install flask-sqlalchemy
        pip3 install wtforms
        pip3 install flask-wtf
     
     -- 设置数据库
     
        使用 mysql 数据库，用户名为 root，密码为 ‘123456’，可以在 db.py 中修改用户名和密码。
        启动 mysql 后，执行数据库脚本 db.sql 创建数据库 todoDB。
     
     -- 运行程序
     
        manage.py 是程序的入口

### 程序的结构

![image](https://user-images.githubusercontent.com/48540417/114809249-6783f800-9ddc-11eb-8a5b-21f09245bbd8.png)

    前端的核心操作如下：
    -- 在 login.html 中，通过 POST 方法向页面 /users/login 提交表单请求完成登录；
    -- 在 register.html 中，通过 POST 方法向页面 /users/register 提交表单请求完成登录；
    -- 访问页面 /users/logout 退出系统；
    -- 在 script.js 中，函数 addTodo () 通过 Ajax 向页面 /todos/add 请求增加待做事项；
    -- 在 script.js 中，函数 updateTodo () 通过 Ajax 向页面 /todos/update 请求更新待做事项；
    -- 在 script.js 中，函数 deleteTodo () 通过 Ajax 向页面 /todos/delete 请求删除待做事项。
    
    后端的核心操作如下：
    -- Flask 程序使用了 2 个蓝图：users 和 todos；
    -- 蓝图 users 定义了页面 /users/login 、/users/register、/users/logout，登录和注册的页面处理函数是 login 和 register，最终调用 db.js 中的数据库访问函数 login 和 register，实现登录和注册的功能；
    -- 蓝图 todos 定义了页面 /todos/add、/todos/update、/todos/delete，它们的页面处理函数是 addTodo、updateTodo、deleteTodo，最终调用 db.js 中的数据库访问函数 addTodo、updateTodo、deleteTodo，实现增加、更新、删除待做事项的功能。

## 2. 后端实现

      -- 数据库设计
            -- 表的设计
            -- 数据库脚本 db.sql
      -- Flask 实例 __init__.py
      -- 入口 manage.py
            -- 导入相关模块
      -- 数据库访问 db.py
            -- 导入相关模块并配置
            -- 映射表 users 和表 todos
            -- 对表 users 进行操作
            -- 对表 todos 进行操作
      -- 视图函数 home.py
            -- 导入相关模块
            -- 页面 / 的视图函数
      -- 蓝图 users.py
            -- 导入相关模块
            -- 登录表单
            -- 请求 /users/login 页面
            -- 注册表单
            -- 请求 /users/register 页面
            -- 退出系统 /logout
      -- 蓝图 todos.py
            -- 导入相关模块
            -- 请求 /todos/add 页面
            -- 请求 /todos/update 页面
            -- 请求 /todos/delete 页面

## 3. 前端实现

    -- 首页模板 index.html
        -- 引入相关的库
        -- 显示 “登录/注册” 按钮
        -- 输入待做事项的文本框
        -- 待做清单和完成清单
    -- 注册页面模板 register.html
        -- 引入相关文件
        -- 注册表单
    -- 登录页面模板 login.html
    
    -- 调用后端服务 script.js
        -- 配置 Ajax
        -- 新增待做事项
        -- 更新待做事项
        -- 删除待做事项
    
    -- 样式文件 style.css