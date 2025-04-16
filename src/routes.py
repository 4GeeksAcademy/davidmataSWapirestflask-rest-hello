from flask import request, jsonify
from .models import db, People, Planet, Vehicle, User, Favorite
from . import api


# --------- PEOPLE ---------
@api.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    return jsonify([p.serialize() for p in people]), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_single_person(people_id):
    person = People.query.get(people_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(person.serialize()), 200


# --------- PLANETS ---------
@api.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    return jsonify([p.serialize() for p in planets]), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    return jsonify(planet.serialize()), 200


# --------- VEHICLES ---------
@api.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([v.serialize() for v in vehicles]), 200

@api.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_single_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(vehicle.serialize()), 200


# --------- USERS ---------
@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([u.serialize() for u in users]), 200


# --------- FAVORITES ---------
@api.route('/users/favorites', methods=['GET'])
def get_all_favorites_for_user():
    # Simulación de "usuario actual", usando user_id = 1 por ahora
    user = User.query.get(1)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify([fav.serialize() for fav in user.favorites]), 200


@api.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user = User.query.get(1)
    if not user:
        return jsonify({"error": "User not found"}), 404
    person = People.query.get(people_id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    fav = Favorite(user_id=user.id, people_id=person.id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.serialize()), 201


@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.get(1)
    if not user:
        return jsonify({"error": "User not found"}), 404
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    fav = Favorite(user_id=user.id, planet_id=planet.id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.serialize()), 201


@api.route('/favorite/vehicle/<int:vehicle_id>', methods=['POST'])
def add_favorite_vehicle(vehicle_id):
    user = User.query.get(1)
    if not user:
        return jsonify({"error": "User not found"}), 404
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    fav = Favorite(user_id=user.id, vehicle_id=vehicle.id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(fav.serialize()), 201


@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    fav = Favorite.query.filter_by(user_id=1, people_id=people_id).first()
    if not fav:
        return jsonify({"error": "Favorite not found"}), 404
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"message": "Favorite removed"}), 200


@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    fav = Favorite.query.filter_by(user_id=1, planet_id=planet_id).first()
    if not fav:
        return jsonify({"error": "Favorite not found"}), 404
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"message": "Favorite removed"}), 200


@api.route('/favorite/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_favorite_vehicle(vehicle_id):
    fav = Favorite.query.filter_by(user_id=1, vehicle_id=vehicle_id).first()
    if not fav:
        return jsonify({"error": "Favorite not found"}), 404
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"message": "Favorite removed"}), 200
