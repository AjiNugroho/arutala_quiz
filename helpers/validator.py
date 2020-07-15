# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import request, Response, g
from functools import wraps
from helpers.response_builder import resp


def client_checker(no_auth=False, role='', features=''):
    """nanti diperlukan untuk authentikasi
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            #episode_id = kwargs.get('episode_id')
            #post_id = kwargs.get('post_id')
            token = request.headers.get('token', None)
            get_json = request.get_json(force=True, silent=True)
            if get_json:
                request_params = get_json
            else:
                request_params = request.form

            #nanti kalau butuh pakai token
            if token is None:

                if no_auth:
                    # kalau mengirimkan parameter no_auth
                    # data token menjadi optional
                    # request akan tetap diproses tanpa perlu data user
                    return f(request_params=request_params, *args, **kwargs)
                else:
                    return resp(401)

            # di sini mulai proses authentikasi token

            return f(
                request_params=request_params,
                *args,
                **kwargs)

        return decorated_function
    return decorator
