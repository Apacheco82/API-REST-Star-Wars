from flask import request, jsonify
from models.index import db, People
import domain.people.controller as Controller #se importan todas las funciones del controller, si se hace asi vienen todas y no una a una

def people_route(app):

    @app.route('/people', methods=['GET'])
    def get_people():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_people()


    @app.route('/people/<int:id>', methods=['GET'])
    def get_single_people(id):  # el id se pasa como param de la funcion
       return Controller.get_single_people(id) # el id se pasa como param de la funcion

    #CREATE USER
    @app.route('/people', methods=['POST'])
    def create_people():
        body = request.get_json()
        return Controller.create_people(body), 201


    @app.route('/people/<int:id>', methods=['PUT'])
    def modify_people(id):
        return Controller.modify_people(id)


    @app.route('/people/<int:id>', methods=['DELETE'])
    def delete_people(id):
        return Controller.delete_people(id)