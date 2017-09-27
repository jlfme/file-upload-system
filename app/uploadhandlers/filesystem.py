#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import mimetypes
from app.uploadhandlers import BaseUploadHandler
from flask import current_app, safe_join
from app.uploadhandlers.utils import etag_stream


class FileUploadHandler(BaseUploadHandler):

    def new(self, file):
        """ 上传新的文件到文件系统

        :param file: <class 'werkzeug.datastructures.FileStorage'> instance
        :return:
        """

        upload_dir = current_app.config.get('UPLOAD_DIR')
        file_path = safe_join(upload_dir, self.new_filename(file))

        print(file.stream)

        from datetime import datetime
        obj = self.model(content_length=len(file.stream.read()),
                         content_type=file.content_type,
                         filename=file.filename,
                         path=file_path,
                         url="dddddddddddddd",
                         upload_date=datetime.utcnow())
        self.db.session.add(obj)
        self.db.session.commit()

        file.save(file_path)

    def delete(self, filename):
        pass

    def get(self, filename):
        pass

    def all(self):
        pass
