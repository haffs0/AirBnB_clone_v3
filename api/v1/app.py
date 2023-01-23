#!/usr/bin/python3
"""main app setup for Flask instance in REST API"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exc=None):
    """teardown of app context of flask"""
    storage.close()


if __name__ == '__main__':
    """run your Flask server"""
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = 5000
    app.run(host=host, port=port, threaded=True)
