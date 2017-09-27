#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename, allowed_extensions=None):
    """ 检测给定文件名是否允许上传
    :param filename: 文件名
    :return: True or False
    """
    allowed_extensions = allowed_extensions or ALLOWED_EXTENSIONS
    return filename[-3:].lower() in allowed_extensions
