#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import os
from app.utils.random import secret_key


class Config:

    # secret_key for session
    SECRET_KEY = secret_key()

    # SQLALCHEMY_ECHO = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password123@10.10.10.4:3306/flask_upload'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # mongodb
    MONGO_HOST = '10.10.10.4'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'cnav'

    # flask_wtf
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = secret_key()

    # per_page
    FILM_PER_PAGE = 40
    PER_PAGE = 100

    # 文件上传相关配置
    APP_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # 图片上传目录
    UPLOAD_DIR = os.path.abspath(os.path.join(APP_BASE_DIR, '.././upload/'))
    # 上传目录不存在就创建
    if not os.path.exists(UPLOAD_DIR):
        os.mkdir(UPLOAD_DIR)

    # 允许文件类型
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']

    # 文件最大尺寸
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


config_mapping = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
