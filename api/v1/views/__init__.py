#!/usr/bin/python3
''' Sets a new flask obj based on app blueprint '''

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
