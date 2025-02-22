#!/usr/bin/python3
"""Create a new view for State objects
that handles all RESTful API actions"""

from flask import jsonify, abort, request, Response
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'],
                 strict_slashes=False)
def get_cities(state_id=None):
    """ Handles HTTP request of all the city obj """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        if 'name' not in data:
            return Response("Missing name", 400)
        city = City(name=data.get('name'), state_id=state.id)
        city.save()
        return jsonify(city.to_dict()), 201

    all_cities = storage.all('City')
    cities = []

    for city in all_cities.values():
        if city.state_id == state.id:
            cities.append(city.to_dict())
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def get_city(city_id=None):
    """ Handles HTTP requests of a single city obj """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    if request.method == 'DELETE':
        storage.delete(city)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return Response("Not a JSON", 400)
        data['id'] = city.id
        data['created_at'] = city.created_at
        data['state_id'] = city.state_id
        city.__init__(**data)
        city.save()
        return jsonify(city.to_dict()), 200

    return jsonify(city.to_dict())
