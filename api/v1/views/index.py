#!/usr/bin/python3
"""index file of REST API
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def service_status():
    """return the status of your API"""
    return jsonify({'status': 'OK'})
