# -*- coding: utf-8 -*-

"""
    application
    ~~~~~~~~~~~
"""

import sys
#from flask.ext.assets import Bundle
from factory import AppFactory
from settings import DevelopmentConfig
#from libs.ext import assets

#update sys to utf-8
reload(sys)
sys.setdefaultencoding('utf8')

app = AppFactory(DevelopmentConfig).get_app(__name__)


# Assets zone

#css_base_bundle = ['css/reset.css', 'css/typo.css', 'css/style.css',
#                   'css/page.css', 'css/forms.css']
#
#css_base = Bundle(*css_base_bundle, filters='cssmin', output='gen/base.css')
#assets.register('css_base', css_base)
#
#js_base_bundle = ['js/libs/json2.js', 'js/libs/jquery-1.8.2-min.js',
#                  'js/libs/underscore-1.4.2-min.js', 'js/libs/backbone-0.9.2-min.js']
#
#js_base = Bundle(*js_base_bundle, filters='jsmin', output='gen/base.js')
#assets.register('js_base', js_base)
