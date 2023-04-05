from flask import request, jsonify
from models.index import db, Planet
import domain.user.controller as Controller

def planets_route(app):

    @app.route('/planets', methods=['GET'])
    def get_planets():
        all_planets = Planet.query.all()
        # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
        planet_serialized = list(
            map(lambda planet: planet.serialize(), all_planets))
        return planet_serialized


    # se añade esto para que coja el int del id
    @app.route('/planets/<int:id>', methods=['GET'])
    def get_single_planet(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase Planet, metodo query.get pasandole el id como param
        planet = Planet.query.get(id)
        return jsonify(planet.serialize()), 200


    @app.route('/planets', methods=['POST'])
    def create_planet():
        data = request.get_json()
        planet = Planet(name=data['name'],  # Agrega el nombre del planeta
                        rotation_period=data['rotation_period'],
                        orbital_period=data['orbital_period'],
                        diameter=data['diameter'],
                        climate=data['climate'],
                        gravity=data['gravity'],
                        terrain=data['terrain'],
                        surface_water=data['surface_water'],
                        population=data['population'])
        db.session.add(planet)
        db.session.commit()

        response = {
            "result": {
                "planets": planet.serialize(),
            }
        }
        return response, 201


    @app.route('/planets/<int:id>', methods=['PUT'])
    def modify_planet(id):
        planet = Planet.query.get(id)
        if not planet:
            return jsonify({'error': 'El planeta no existe'}), 404

        data = request.get_json()
        planet.name = data['name']
        planet.rotation_period = data['rotation_period']
        planet.orbital_period = data['orbital_period']
        planet.diameter = data['diameter']
        planet.climate = data['climate']
        planet.gravity = data['gravity']
        planet.terrain = data['terrain']
        planet.surface_water = data['surface_water']
        planet.population = data['population']

        db.session.commit()

        return jsonify(planet.serialize()), 200

    @app.route('/planets/<int:id>', methods=['DELETE'])
    def delete_planet(id):
        planet = Planet.query.get(id)
        if not planet:
            return jsonify({'error': 'El planeta no existe'}), 404

        db.session.delete(planet)
        db.session.commit()

        return '', 204