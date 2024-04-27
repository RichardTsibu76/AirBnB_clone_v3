#!/usr/bin/python3

"""Handles endpoints"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def get_status():
    """Returns the status of the API service."""
    return jsonify({"status": "OK"})
