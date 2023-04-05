from flask import request, jsonify
from models.index import db, Starship
import domain.user.controller as Controller

def starships_route(app):
    @app.route('/starships', methods=['GET'])
    def get_starships():
        all_starships = Starship.query.all()
        # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
        starship_serialized = list(
            map(lambda starship: starship.serialize(), all_starships))
        return starship_serialized


    # se añade esto para que coja el int del id
    @app.route('/starships/<int:id>', methods=['GET'])
    def get_single_starship(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase Planet, metodo query.get pasandole el id como param
        starship = Starship.query.get(id)
        return jsonify(starship.serialize()), 200


    @app.route('/starships', methods=['POST'])
    def create_starship():
        data = request.get_json()
        starship = Starship(name=data['name'],
                        model=data['model'],
                        manufacturer=data['manufacturer'],
                        starship_class=data['starship_class'],
                        cost_in_credits=data['cost_in_credits'],
                        length=data['length'],
                        crew=data['crew'],
                        passengers=data['passengers'],
                        max_atmosphering_speed=data['max_atmosphering_speed'],
                        hyperdrive_rating=data['hyperdrive_rating'],
                        mglt=data['mglt'],
                        cargo_capacity=data['cargo_capacity'],
                        consumables=data['consumables'])
        db.session.add(starship)
        db.session.commit()

        response = {
            "result": {
                "starships": starship.serialize()
            }
        }
        return response, 201

    @app.route('/starships/<int:id>', methods=['PUT'])
    def modify_starship(id):
        starship = Starship.query.get(id)
        if not starship:
            return jsonify({'error': 'El vehiculo no existe'}), 404

        data = request.get_json()
        starship.name = data['name']
        starship.model = data['model']
        starship.manufacturer = data['manufacturer']
        starship.starship_class = data['diameter']
        starship.cost_in_credits = data['cost_in_credits']
        starship.length = data['length']
        starship.crew = data['crew']
        starship.passengers = data['passengers']
        starship.max_atmosphering_speed = data['max_atmosphering_speed']
        starship.cargo_capacity = data['cargo_capacity']
        starship.consumables = data['consumables']
        starship.hyperdrive_rating = data['hyperdrive_rating']
        starship.mglt = data['mglt']
        starship.pilots = data['pilots']

        db.session.commit()

        return jsonify(starship.serialize()), 200

    @app.route('/starships/<int:id>', methods=['DELETE'])
    def delete_starship(id):
        starship = Starship.query.get(id)
        if not starship:
            return jsonify({'error': 'El vehiculo no existe'}), 404

        db.session.delete(starship)
        db.session.commit()

        return '', 204