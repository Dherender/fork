# -*- coding: utf-8 -*-

"""
"""

from flask import url_for
from testing import KitTestCase


class TestFrontBlueprint(KitTestCase):

    def test_front(self):
        response = self.client.get(url_for('web.home_ui'))
        self.assert200(response)

    def test_front_for_anonymous(self):
        response = self.client.get(url_for('web.home_ui'))
        self.assertContains(response, 'Log in')

    def test_login(self):
        response = self.client.get(url_for('web.login_ui'))
        self.assert200(response)
