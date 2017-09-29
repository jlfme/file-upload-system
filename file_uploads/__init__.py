#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import os
import warnings


class FileUploader(object):

    def __init__(self):
        self.uploader_type = None

    def init_app(self, app, uploader_type='filesystem'):
        """
        :param app:
        :param uploader_type:
        :return:
        """
        self.uploader_type = uploader_type

        if 'FILE_UPLOAD_DIR' not in app.config:
            # 文件上传相关配置
            APP_BASE_DIR = app.config.get('APP_BASE_DIR')
            # 图片上传目录
            FILE_UPLOAD_DIR = os.path.abspath(os.path.join(APP_BASE_DIR, '.././upload/'))
            # 上传目录不存在就创建
            if not os.path.exists(FILE_UPLOAD_DIR):
                os.mkdir(FILE_UPLOAD_DIR)

            warnings.warn(
                'FILE_UPLOAD_DIR not set. Defaulting to {}'.format(FILE_UPLOAD_DIR)
            )

        # app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')

    def uploader(self):
        if self.uploader_type is None:
            raise Exception("")
        if self.uploader_type == 'filesystem':
            from .uploaders.filesystem import FileSystemUploader
            return FileSystemUploader


if __name__ == '__main__':
    APP_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # 图片上传目录
    UPLOAD_DIR = os.path.abspath(os.path.join(APP_BASE_DIR, '.././upload/'))
    # 上传目录不存在就创建
    # if not os.path.exists(UPLOAD_DIR):
    #     os.mkdir(UPLOAD_DIR)
