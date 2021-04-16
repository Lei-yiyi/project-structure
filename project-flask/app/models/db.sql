-- 数据库设计

/*
（1）表的设计

在数据库中存在 users 和 todos 两张表：

-- 表 users 用于记录已经注册的用户，包含有如下字段及描述：
userId    用户的 ID（表的主键）
name      姓名
password  密码

-- 表 todos 用于记录待做事项，包含有如下字段及描述：
todoId  待做事项的 ID（表的主键）
userId  所属用户的 ID
status  待做事项的状态（“todo” 表示待做，“done” 表示已经完成）
title   待做事项的标题

（2）数据库脚本（见下面脚本）
*/

-- 1. 创建数据库 todoDB

-- 如果数据库 todoDB 已经存在，则首先删除，然后再创建数据库 todoDB。
SET character_set_database=utf8;
SET character_set_server=utf8;
DROP DATABASE IF EXISTS todoDB;
CREATE DATABASE todoDB;
USE todoDB;

-- 2. 创建表 users

-- 创建表 users，表 users 包含 userId、name、password 等字段。userId 是主键，设置为从 1 自动增长。
CREATE TABLE users(
    userId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY(userId)
);

-- 3. 创建表 todos

-- 创建表 todos，表 todos 包含 todoId、userId、status、title 等字段。todoId 是主键，设置为从 1 自动增长。
CREATE TABLE todos(
    todoId INT NOT NULL AUTO_INCREMENT,
    userId INT,
    status VARCHAR(255),
    title VARCHAR(255),
    PRIMARY KEY(todoId)
);

-- 4. 创建测试数据

-- 为了方便测试，向数据库中插入一些预定义的数据。
INSERT INTO users(name, password) VALUES ("guest", "123");
INSERT INTO todos(userId, status, title) VALUES (1, "todo", "吃饭");
INSERT INTO todos(userId, status, title) VALUES (1, "todo", "睡觉");
INSERT INTO todos(userId, status, title) VALUES (1, "done", "作业");