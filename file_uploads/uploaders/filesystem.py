#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


from datetime import datetime
from flask import current_app, safe_join, send_from_directory, url_for
from app.uploadhandlers.uploaders import BaseFileUploader


class FileSystemUploader(BaseFileUploader):

    def save(self, file):
        """ 上传新的文件到文件系统

        :param file: <class 'werkzeug.datastructures.FileStorage'> instance
        :return:
        """
        file_stream = file.stream
        filename = self.new_filename(file.content_type, file_stream)
        file_path = safe_join(current_app.config.get('UPLOAD_DIR'), filename)
        content_length = len(file_stream.read())

        obj = self.model(content_length=content_length,
                         content_type=file.content_type,
                         filename=filename,
                         path=file_path,
                         etag=filename,
                         url=url_for('upload.picture_get', filename=filename),
                         upload_date=datetime.now())
        self.db.session.add(obj)
        self.db.session.commit()
        # save file
        file_stream.seek(0)
        file.save(file_path)
        file_stream.close()

        return obj

    def delete(self, filename):
        pass

    def get(self, filename):
        options = {
            'cache_timeout': 60 * 60 * 24
        }
        return send_from_directory(current_app.config['UPLOAD_DIR'], filename, **options)

    def all(self):
        pass
