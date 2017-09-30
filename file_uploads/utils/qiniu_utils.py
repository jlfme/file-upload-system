#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-29 15:44:18
# ---------------------------------------


from qiniu import Auth, BucketManager, put_data

from flask import current_app


def get_auth(access_key, secret_key):
    return Auth(access_key, secret_key)


def make_upload_token(access_key, secret_key, bucket_name, expires=3600):
    q = get_auth(access_key, secret_key)
    token = q.upload_token(bucket=bucket_name, expires=expires)
    return token


def upload_file(key, data):
    access_key = current_app.config.get('QINIU_ACCESS_KEY')
    secret_key = current_app.config.get('QINIU_SECRET_KEY')
    bucket_name = current_app.config.get('QINIU_BUCKET_NAME')

    up_token = make_upload_token(access_key, secret_key, bucket_name, expires=365 * 24 * 3600)
    return put_data(up_token, key, data)


def delete_file(key):
    bucket_name = current_app.config.get('QINIU_BUCKET_NAME')
    access_key = current_app.config.get('QINIU_ACCESS_KEY')
    secret_key = current_app.config.get('QINIU_SECRET_KEY')

    bucket = BucketManager(get_auth(access_key, secret_key))
    ret, info = bucket.delete(bucket_name, key)
    return ret, info
