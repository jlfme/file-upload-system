#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import os
import warnings


class FileUploaderConfigError(Exception):
    """
    This exception is raised if the uploader configuration  was error.
    """
    pass


class FileUploader(object):

    """
    Attributes:
        app:
        uploader_type:
    """

    def __init__(self, app=None, uploader_type=None, db=None):
        self.uploader_type = uploader_type
        self.db = db
        if app is not None and db is not None:
            self.init_app(app, db)

    def init_app(self, app, db):
        """
        :param app: The `~flask.Flask` instance
        :param db: The `~flask_sqlalchemy.SQLAlchemy` instance
        :param uploader_type: str: 'filesystem'|'qiniu'|'mongodb'

        """

        self.db = db

        if self.uploader_type is None and 'FILE_UPLOADER_TYPE' not in app.config:
            warnings.warn("FILE_UPLOADER_TYPE not set. Defaulting to 'filesystem'")
            app.config.setdefault('FILE_UPLOADER_TYPE', 'filesystem')
            self.uploader_type = app.config.get('FILE_UPLOADER_TYPE')

        if self.uploader_type == 'filesystem':
            if 'FILE_UPLOAD_DIR' not in app.config:
                file_upload_dir = os.path.abspath(
                    os.path.join(app.config.get('APP_BASE_DIR'), './upload/')
                )

                if not os.path.exists(file_upload_dir):
                    os.mkdir(file_upload_dir)

                app.config.setdefault('FILE_UPLOAD_DIR', file_upload_dir)
                warnings.warn(
                    "FILE_UPLOAD_DIR not set. Defaulting to '{}'".format(file_upload_dir)
                )

        elif self.uploader_type == 'qiniu':
            for item in ['QINIU_ACCESS_KEY', 'QINIU_SECRET_KEY', 'QINIU_BUCKET_NAME', 'QINIU_BUCKET_DOMAIN']:
                if item not in app.config:
                    raise FileUploaderConfigError("{} not set.".format(item))

        elif self.uploader_type == 'mongodb':
            pass

        else:
            raise FileUploaderConfigError()


    def uploader(self):
        if self.uploader_type is None:
            raise Exception("")
        if self.uploader_type == 'filesystem':
            from .uploaders.filesystem import FileSystemUploader
            return FileSystemUploader(db=self.db)
        elif self.uploader_type == 'qiniu':
            from .uploaders.qiniu import QiNiuUploader
            return QiNiuUploader(db=self.db)
