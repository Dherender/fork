# -*- coding: utf-8 -*-

"""
    login ui
"""

from flask.ext.mako import render_template

from web import web_bp

@web_bp.route('/login')
def login_ui():
    return render_template('login.html', **locals())
