#!/usr/bin/python3
'''
Creating a new view for amentiy
'''

from flask import abort, request, jsonify
from api.v1.views import app_view
from models import storage
from models.amenity import Amenity


@app_views.route("/amenities/<amenity_id>/amenities", methods=["GET"])
def get_amenity(amenity_id):
    """
    Retrieve all amenties.
    """

    state = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route("/amenity/<amenity_id>", methods=["GET"])
def get_amenity_id(amenity_id):
    """
    Retrieve a amenity by its ID.

    Args:
        amenity_id (str): The ID of the amenity to retrieve.

    Returns:
        dict: A JSON representation of the city.

    Raises:
        404: If the amenity with the specified ID does not exist.
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    '''
    Delete a amenity based on its ID.

    Args:
        amenity_id (str): The ID of the amenity to be deleted.

    Returns:
        tuple: A tuple containing an empty JSON response and a status code of
        200.
    '''

    obj = storage.get(Amenity, amenity_id)
    if obj is None:
        abort(404)

    storage.delete(obj)
    return jsonify({}), 200


@app_views.route("/amenities/<amenity_id>/amenities", methods=["POST"])
def create_amenity(amenity_id):
    '''
    create a new amentiy
    '''

    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    data = request.get_json(force=True, silent=True)

    # the data provided must be a dictionary
    if not data or not isinstance(data, dict):
        abort(400, "Not a JSON")

    if "name" not in data:
        abort(400, "Missing name")

    new_amenity = City(state_id=state.id, **data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    """
    Update amenity with the given amenity_id.
    """
    amenity_obj = storage.get(Amenity, amenity_id)
    if amenity_obj is None:
        abort(404)

    data = request.get_json(force=True, silent=True)
    # the data provided must be a dictionary
    if not data or not isinstance(data, dict):
        abort(400, "Not a JSON")

    if "name" not in data:
        abort(400, "Missing name")

    for key, value in data.items():
        if key in ['id', 'created_at', 'updated_at', 'state_id']:
            continue

        setattr(amenity_obj, key, value)

    amenity_obj.save()
    return jsonify(amenity_obj.to_dict()), 200
