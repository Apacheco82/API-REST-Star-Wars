from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller #se importan todas las funciones del controller, si se hace asi vienen todas y no una a una

def user_route(app):

    @app.route('/user', methods=['GET'])
    def get_users():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_users()


    @app.route('/user/<int:id>', methods=['GET'])
    def get_single_user(id):  # el id se pasa como param de la funcion
       return Controller.get_single_user(id) 

    
    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        return Controller.create_user(body), 201


    @app.route('/user/<int:id>', methods=['PUT'])
    def modify_user(id):
        return Controller.modify_user(id)


    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
        return Controller.delete_user(id)
