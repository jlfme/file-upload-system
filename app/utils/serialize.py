#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import mimetypes
import re
from flask import url_for, current_app


def order_name(name):
    """整理文件名, 最大显示20个字符, 如果长度大于20个字符就在中间加上省略号
    :param name: 文件名字符
    """
    name = re.sub(r'^.*/', '', name)
    if len(name) <= 20:
        return name
    return name[:10] + "..." + name[-7:]


def serialize(instance):
    """serialize -- Serialize a Picture instance into a dict.

    Args:
        instance: `class models.Picture` a object

    Returns:
        dict:

    """

    url = url_for('main.picture_get', filename=instance.filename)
    uploader_type = current_app.config.get('FILE_UPLOADER_TYPE')

    if uploader_type == 'qiniu':
        # url = current_app.config.get('')
        url = "http://owoorc7te.bkt.clouddn.com/" + instance.filename

    return {
        'url': url,
        'name': order_name(instance.filename),
        'type': mimetypes.guess_type(instance.filename)[0] or 'image/jpeg',
        'thumbnailUrl': url,
        'size': instance.content_length,
        'deleteUrl': url_for('main.picture_delete', pk=instance.id),
        'deleteType': 'DELETE',
    }
