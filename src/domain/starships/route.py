from flask import request, jsonify
from models.index import db, Starship
import domain.starships.controller as Controller

def starships_route(app):

    @app.route('/starships', methods=['GET'])
    def get_starships():
        return Controller.get_starships()


    # se añade esto para que coja el int del id
    @app.route('/starships/<int:id>', methods=['GET'])
    def get_single_starship(id):  # el id se pasa como param de la funcion
       return Controller.get_single_starship(id) # el id se pasa como param de la funcion


    @app.route('/starships', methods=['POST'])
    def create_starship():
        body = request.get_json()
        return Controller.create_starship(body), 201


    @app.route('/starships/<int:id>', methods=['PUT'])
    def modify_starship(id):
        return Controller.modify_starship(id)

    @app.route('/starships/<int:id>', methods=['DELETE'])
    def delete_starship(id):
        return Controller.delete_starship(id)