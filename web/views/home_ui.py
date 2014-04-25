# -*- coding: utf-8 -*-

"""
    home ui
"""

from flask.ext.mako import render_template

from web import web_bp

@web_bp.route('/', methods=['GET'])
def home_ui():
    return render_template('index.html', **locals())
