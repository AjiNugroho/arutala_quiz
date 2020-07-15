# -*- coding: utf-8 -*-
# !/usr/bin/env python


class TestController(object):

    def test_get_c(self, client):
        '''Method ini untuk ngetest controller'''
        
        #test end point yang ada, status_code => 200
        res = client.get("bill")
        assert res.status_code == 200
        assert type(res.json) == dict
        assert len(res.json) > 0

        # test end point yang tidak ada -> 404
        res = client.get("boll")
        assert res.status_code == 200
        assert res.json['error']['code'] == 404
