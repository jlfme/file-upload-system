#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Picture(db.Model):

    __tablename__ = 'upload_picture'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    etag = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    content_type = db.Column(db.String(50), nullable=True)
    content_length = db.Column(db.BigInteger, nullable=True)
    upload_date = db.Column(db.DateTime, nullable=False)
