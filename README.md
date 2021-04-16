# Project structure

## Flask的项目结构 —— project-flask
目录结构：

    ├── app  -- 项目的主要功能实现
    │   ├── __init__.py
    │   ├── app1
    │   │   ├── __init__.py
    │   │   └── views.py            # 视图文件
    │   ├── app2
    │   │   ├── __init__.py
    │   │   ├── forms.py            # 表单文件
    │   │   ├── templates           # 模板文件
    │   │   │   └── *.html
    │   │   └── views.py 
    │   ├── app3
    │   │   ├── __init__.py
    │   │   ├── models.py           # 数据库模型文件
    │   │   ├── static              # 静态资源文件
    │   │   │   ├── *.css
    │   │   │   └── *.js
    │   │   ├── templates
    │   │   │   └── *.html
    │   │   └── views.py
    │   └── extensions.py           # 各种扩展
    ├── migrations/       # 数据迁移文件夹
    ├── venv/             # 虚拟环境
    ├── tests/            # 单元测试程序
    ├── config.py         # 全局配置文件，配置全局变量
    ├── fabfile.py        # 使用Fabric3完成项目发布工作的脚本
    ├── manage.py         # 项目启动控制文件
    ├── README.md  -- 仓库的说明，比如该项目的介绍等
    └── requirements.txt  # 项目所依赖的第三方包以及版本号，方便在其他位置生成相同的虚拟环境以及依赖  

组织蓝图：

    目前主要有两种组织方式：
    - 按照 功能结构 组织。模板在一个文件夹中，静态文件在另外一个文件夹中，视图在第三个文件夹中。
    - 按照 分区 组织。同一个功能的模板，静态文件，视图都在一个文件夹内。
    两种组织方式的优劣并无定论。上文中是按照 分区 进行组织的。下文中是按照 功能结构 进行组织的。


    ├── app  -- 项目的主要功能实现
    │   ├── __init__.py   
    │   ├── forms               # 表单文件
    │   │   ├── __init__.py
    │   │   └── *.py
    │   ├── models              # 数据库模型文件
    │   │   ├── __init__.py
    │   │   └── *.py
    │   ├── static              # 静态资源文件
    │   │   └── *.css
    │   │   └── *.js
    │   ├── templates           # 模板文件
    │   │   └── *.html
    │   ├── views               # 视图文件
    │   │   ├── __init__.py
    │   │   └── *.py
    └── └── extensions.py       # 各种扩展
