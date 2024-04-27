#!/usr/bin/python3

"""This module contains routes for the app."""

import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(_):
    """Handles session teardown operation."""
    storage.close()


if __name__ == "__main__":
    app.run(host=f"{os.getenv('HBNB_API_HOST') or '0.0.0.0'}",
            port=f"{os.getenv('HBNB_API_PORT') or 5000}", threaded=True)
