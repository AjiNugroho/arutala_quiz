# -*- coding: utf-8 -*-
# !/usr/bin/env python

from app.rest_api.models import Database

class TestModel(object):
    """
    Untuk test model
    """

    def test_get_m(self, app_context):
        """

        :param app_context:
        :return:
        """

        db = Database()
        db_resp = db.get_bill()
        assert type(db_resp) == dict
