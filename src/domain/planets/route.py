from flask import request, jsonify
from models.index import db, Planet
import domain.planets.controller as Controller

def planets_route(app):

    @app.route('/planets', methods=['GET'])
    def get_planets():
        return Controller.get_planets()


    # se añade esto para que coja el int del id
    @app.route('/planets/<int:id>', methods=['GET'])
    def get_single_planet(id):  # el id se pasa como param de la funcion
       return Controller.get_single_planet(id) # el id se pasa como param de la funcion


    @app.route('/planets', methods=['POST'])
    def create_planet():
        body = request.get_json()
        return Controller.create_planet(body), 201


    @app.route('/planets/<int:id>', methods=['PUT'])
    def modify_planet(id):
        return Controller.modify_planet(id)

    @app.route('/planets/<int:id>', methods=['DELETE'])
    def delete_planet(id):
        return Controller.delete_planet(id)