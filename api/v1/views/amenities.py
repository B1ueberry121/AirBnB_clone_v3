#!/usr/bin/python3
"""Creates a new view for Amenities object"""

from flask import jsonify, abort, request, Response
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities/', methods=['GET', 'POST'],
                 stict_slashes=False)

def get_amenities():
    """Handles HTTP request for all amenities"""

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        if 'name' not in data:
            return Response("Missing name", 400)
        amenity = Amenity(name=data.get('name'), state_id=state.id)
        amenity.save()
        return jsonify(amenity.to_dict()), 201

    all_amenities = storage.all('Amenity')
    amenities = []

    for amenity in all_amenities.values():
        amenities.append(amenity to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'],
                 stict_slashes=False)

def get_amenity(amenity_id=None):
    """Handles HTTP request of a single amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is none:
        abort (404)

    if request.method == 'DELETE':
        sorage.delete(amenity)
        storage.seave()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        data['id'] = amenity_id
        data['created_at'] = amenity.created_at
        amenity.__init__(**data)
        amenity.save()
        return jsonify(amenity.to_dict()), 200

    return jsonify(amenity.to_dict)
