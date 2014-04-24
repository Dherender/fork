# -*- coding: utf-8 -*-

"""
    settings
    ~~~~~~~~

    Global settings for project.

"""

import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "fork_tofu"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    MAKO_TRANSLATE_EXCEPTIONS = False

    BLUEPRINTS = ['web.web_bp',
                  ]

    EXTENSIONS = ['libs.ext.db',
                  'libs.ext.assets',
                  'libs.ext.login_manager',
                  'libs.ext.mako',
                  ]

#    CONTEXT_PROCESSORS = ['base.context_processors.common_context',
#                          'base.context_processors.navigation',
#                          'base.context_processors.common_forms',
#                          ]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
