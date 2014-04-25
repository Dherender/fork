# -*- coding: utf-8 -*-
from flask import Blueprint


web_bp = Blueprint('web', __name__,
                 template_folder='templates',
                 url_prefix='')

import views
