# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, os, pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

import main
from helpers.mysql_connect import Database


@pytest.fixture
def app():
    
    app = main.app
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def app_context(app):
    
    with app.app_context() as app_context:
        # setup db
        connection = Database()
        app_context.g.cursor = connection.query
        app_context.g.cursor('SET NAMES UTF8MB4')
        app_context.g.db = connection.db

        yield app_context

        # teardown db
        db = getattr(app_context.g, 'db', None)
        if db is not None:
            db.close()

@pytest.fixture
def request_context(app):
    
    with app.test_request_context() as request_context:
        yield request_context

@pytest.fixture
def client(app):
    
    return app.test_client()
