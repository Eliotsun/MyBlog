# -*- coding: utf-8 -*-
# __auther__ = 'sunshibin'

import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))   # 找到当前根目录

prefix = 'sqlite:////'

# 基本配置类
class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')   # 获取环境密钥

    SQLALCHEMY_TRACK_MODIFICATIONS = False   # 关闭警告信息
    SQLALCHEMY_RECORD_QUERIES = True    # 启用查询记录

    CKEDITOR_ENABLE_CSRF = True  # 开启CSRF保护
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'   # cke富文本编辑器的图片上传

    MYBLOG_POST_PER_PAGE = 7   # 每页文章数
    MYBLOG_MANAGE_POST_PER_PAGE = 15    # 后台管理界面每页文章数
    MYBLOG_COMMENT_PER_PAGE = 5    # 每页评论数
    MYBLOG_MANAGE_COMMENT_PER_PAGE = 15

    MYBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')   # 上传路径
    MYBLOG_ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'png', 'gif', 'jpeg']    # 允许的图片格式


# 开发配置类
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'Myblog.db')   # 设置数据库URI

# 生产配置类
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'Myblog_pd.db'))

# 定义配置映射字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
