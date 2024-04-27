#!/usr/bin/python3

"""Handles endpoints"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def get_status():
    """Returns the status of the API service."""
    return jsonify({"status": "OK"})
