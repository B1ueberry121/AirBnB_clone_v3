#!/usr/bin/python3
'''
    This module handles some routing options for the flask app
'''

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def get_status():
    """ Tests the route status returning a basic JSON query """
    dic = {'status': 'OK'}
    return jsonify(dic)
