#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-29 12:02:18
# ---------------------------------------


import datetime
import mimetypes

from flask import safe_join, current_app
from app.models import Picture, db as database
from ..utils.hash import etag_stream


class BaseFileUploader(object):

    """ all UploadHandler must extends this class

    Attributes:
        model:
        db: SQlAlchemy实例对象

    """

    def __init__(self, model=Picture, db=database, **kwargs):
        self.model = model
        self.db = db
        self.kwargs = kwargs

    def save(self, file):
        raise NotImplementedError

    def delete(self, filename):
        raise NotImplementedError

    def get(self, filename):
        raise NotImplementedError

    def all(self):
        raise NotImplementedError

    def _commit(self):
        self.db.session.commit()

    @staticmethod
    def new_filename(content_type, file_stream):
        """ 根据文件流和文件类型生成文件名

        Args:
            content_type: content_type
            file_stream:  文件的二进制流

        Returns:
            str: new filename

        """

        extension = mimetypes.guess_extension(content_type)
        if extension in ['.jpeg', '.jpe', '.jpg']:
            extension = '.jpg'

        new_name = etag_stream(file_stream) + extension

        if file_stream.tell() > 0:
            file_stream.seek(0)
        return new_name

    def save_file_info(self, filename, content_length, content_type):

        if 'FILE_UPLOAD_DIR' not in current_app.config:
            file_path = ''
        else:
            file_path = safe_join(current_app.config.get('FILE_UPLOAD_DIR'), filename)

        picture = self.model(content_length=content_length,
                             content_type=content_type,
                             filename=filename,
                             path=file_path,
                             etag=filename,
                             upload_date=datetime.datetime.now())
        self.db.session.add(picture)
        self.db.session.commit()

        return picture
