#!/usr/bin/python3
"""
 view for places objects that handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, Flask
from models import storage
from models.place import Place
from models.user import User
from models.city import City


@app_views.route(
        '/cities/<string:city_id>/places',
        methods=['GET', 'POST'],
        strict_slashes=False)
def place(city_id):
    """users route"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(
                [obj.to_dict() for obj in city.places])
    if request.method == 'POST':
        body = request.get_json()
        if body is None or type(body) != dict:
            return jsonify({'error': 'Not a JSON'}), 400
        new_user_id = body.get('user_id')
        if new_user_id is None:
            return jsonify({'error': 'Missing user_id'}), 400
        user = storage.get('User', new_user_id)
        if user is None:
            abort(404)
        new_name = body.get('name')
        if new_name is None:
            return jsonify({'error': 'Missing name'}), 400
        new_place = Place(city_id=city_id, **body)
        new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route(
        '/places/<string:place_id>',
        methods=['GET', 'DELETE', 'PUT'],
        strict_slashes=False)
def places_with_id(place_id):
    """handle places object with parameter state_id"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(place.to_dict())
    if request.method == 'DELETE':
        storage.delete(place)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        put_data = request.get_json()
        if put_data is None or type(put_data) != dict:
            return jsonify({'error': 'Not a JSON'}), 400
        to_ignore = ['id', 'user_id', 'city_id' 'created_at', 'updated_at']
        place.update(to_ignore, **put_data)
        return jsonify(place.to_dict()), 200
