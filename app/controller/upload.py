#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# @author: jlfgeek
# @time: 2017-09-25 01:21:00


from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename
from flask import (jsonify, redirect, abort, request,
                   render_template, current_app, send_from_directory, send_file, safe_join)

from flask_uploads import IMAGES, UploadSet
from app.utils.response import response_mimetype, JSONResponse
from app.models import Picture, db
from app.utils.serialize import serialize
from app.utils.upload import allowed_file


upload_bt = Blueprint(
    'upload',
    __name__,
    template_folder='templates'
)


@upload_bt.route('/upload/picture/<filename>')
def picture_get(filename):
    """根据文件名,从设定的目录中查找并返回文件

    :param filename: 文件名
    :return: 返回指定文件名的文件
    """
    options = {
        'cache_timeout': 60*60*24
    }
    return send_from_directory(current_app.config['UPLOAD_DIR'], filename, **options)


@upload_bt.route('/', methods=['GET', 'POST'])
def picture_new():
    """ 上传文件到设定的目录中
    :return:
    """
    if request.method == 'POST':
        f = request.files['file']
        if f:

            from app.uploadhandlers.filesystem import FileUploadHandler

            handler = FileUploadHandler()

            handler.new(f)



            #
            # pic = Picture(filename=f.filename,
            #               path=file_path,
            #               content_type=f.content_type,
            #               content_length=f.content_length
            #               )
            #
            #
            # print(pic)
            # db.session.add(pic)
            # db.session.commit()

            # data = {'files': [serialize(pic)]}

            return JSONResponse(data=True,
                                mimetype=response_mimetype(request),
                                headers={'Content-Disposition': 'inline; filename=files.json'}
                                )

    return render_template('picture_form.html')


@upload_bt.route('/upload/delete/<int:pk>', methods=['GET', 'DELETE'])
def picture_delete(pk):
    obj = Picture.query.filter_by(id=pk).first()
    if obj:
        db.session.delete(obj)
        db.session.commit()

    return JSONResponse(data=True,
                        mimetype=response_mimetype(request),
                        headers={'Content-Disposition': 'inline; filename=files.json'}
                        )


@upload_bt.route('/upload/view/', methods=['GET'])
def picture_list():
    objects = Picture.query.all()
    for i in objects:
        print(dir(i))
    return 'ok'
