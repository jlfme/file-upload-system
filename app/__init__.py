#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from app.config import config_mapping
from app.models import db
from app.controller import upload


migrate = Migrate()


def create_app(config_name):
    """app factory"""
    app = Flask(__name__)
    app.config.from_object(config_mapping[config_name])

    # 数据库初始化
    db.init_app(app)
    migrate.init_app(app, db)

    # 跨站请求保护
    csrf = CSRFProtect()
    csrf.init_app(app)

    # blueprint
    app.register_blueprint(upload.upload_bt)
    return app
