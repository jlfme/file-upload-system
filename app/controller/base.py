#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-29 15:06:18
# ---------------------------------------


from flask import render_template, redirect
from flask.blueprints import Blueprint


base = Blueprint(
    'upload',
    __name__,
    template_folder='templates'
)


# Sample HTTP error handling
@base.errorhandler(404)
def not_found(error):
    return render_template('404.html', complex={'error': error}), 404


# Index Page
@base.route('/')
def index():
    return redirect('/upload/')
