## 一、项目简介

本项目利用python开发了基于flask和SQLite的个人博客系统，实现个人技术博客的展示。用户上区分为游客及管理员，游客以及依据分类筛选技术博客，阅读技术博
客，在留言区向管理员留言。管理员可以登陆系统，分享个人技术博客，创建分类，阅读处理用户留言等。

## 二、开发环境
    开发系统	Centos 7
    数据库	SQLite 3.7.17
    开发框架	Python-flask
    包依赖	
    flask 	flask框架
	WTForms	表单工具
	Flask-CKEditor	Flask集成富文本编辑器
	Flask-Login	登陆验证
	Python-Dotenv	管理环境变量
	Flask-SQLAlchemy	数据库操作依赖

## 三、部署
使用pipenv部署，安装包依赖后
进入项目执行目录

    cd /blog
执行打开shell环境

    pipenv shell
执行flask

    flask run

    之后打开浏览器访问本地127.0.0.1:5000

管理员账户密码
    
    账户：xixi1216
    密码：helloflask

