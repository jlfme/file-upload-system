#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import mimetypes
from app.models import Picture, db as database
from app.uploadhandlers.utils import etag_stream


class BaseUploadHandler(object):

    """
    Attributes:
        model: Picture model类
        db: SQlAlchemy实例对象
    """

    def __init__(self, model=Picture, db=database, **kwargs):
        self.model = model
        self.db = db
        self.kwargs = kwargs

    def new(self, file):
        pass

    def delete(self, filename):
        pass

    def get(self, filename):
        pass

    def all(self):
        pass

    def _commit(self):
        self.db.session.commit()

    @classmethod
    def etags(cls, input_stream):
        return etag_stream(input_stream)

    @classmethod
    def new_filename(cls, file):
        """ 返回由etag + 文件扩展名组成的新文件名

        Args:
            file: <class 'werkzeug.datastructures.FileStorage'>

        Returns:
            etag + 扩展名
        """

        print(file.stream.read())

        extension = mimetypes.guess_extension(mimetypes.guess_type(file.filename)[0])
        filename = etag_stream(file.stream) + extension
        return filename
