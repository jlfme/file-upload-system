#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


import os
import binascii


def secret_key():
    return binascii.hexlify(os.urandom(24)).decode('utf-8')
