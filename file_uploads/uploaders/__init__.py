#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-29 12:02:18
# ---------------------------------------


import mimetypes

from app.models import Picture, db as database
from app.uploadhandlers.utils.hash import etag_stream


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

    @classmethod
    def etags(cls, file_stream):
        return etag_stream(file_stream)

    @classmethod
    def new_filename(cls, content_type, file_stream):
        """ 返回由etag + 文件扩展名组成的新文件名

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
