from flask import request, jsonify
from models.index import db, People
import domain.user.controller as Controller


def people_route(app):
    @app.route('/people', methods=['GET'])
    def get_people():
        all_people = People.query.all()
        # people_serialized = [people.serialize() for people in all_people] array comprehension
        people_serialized = list(
            map(lambda people: people.serialize(), all_people))
    # people_serialized = [people for people in people] #para vosotros, jugadores
        return people_serialized


    # se añade esto para que coja el int del id
    @app.route('/people/<int:id>', methods=['GET'])
    def get_single_people(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase People, metodo query.get pasandole el id como param
        people = People.query.get(id)
        return jsonify(people.serialize()), 200


    @app.route('/people', methods=['POST'])
    def create_people():
        data = request.get_json()
        people = People(name=data['name'],  # Agrega el nombre del planeta
                        height=data['height'],
                        mass=data['mass'],
                        skin_color=data['skin_color'],
                        eye_color=data['eye_color'],
                        birth_year=data['birth_year'],
                        gender=data['gender'],
                        homeworld_planet=data['homeworld_planet'])
        db.session.add(people)
        db.session.commit()

        response = {
            "result": {
                "people": people.serialize(),
            }
        }
        return response, 201

    @app.route('/people/<int:id>', methods=['PUT'])
    def modify_people(id):
        people = People.query.get(id)
        if not people:
            return jsonify({'error': 'El personaje no existe'}), 404

        data = request.get_json()
        people.name = data['name']
        people.height = data['height']
        people.mass = data['mass']
        people.skin_color = data['skin_color']
        people.eye_color = data['eye_color']
        people.birth_year = data['birth_year']
        people.gender = data['gender']
        people.homeworld_planet = data['homeworld_planet']
        

        db.session.commit()

        return jsonify(people.serialize()), 200

    @app.route('/people/<int:id>', methods=['DELETE'])
    def delete_people(id):
        people = People.query.get(id)
        if not people:
            return jsonify({'error': 'El personaje no existe'}), 404

        db.session.delete(people)
        db.session.commit()

        return '', 204