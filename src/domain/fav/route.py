from flask import request, jsonify
from models.index import db, Fav
import domain.fav.controller as Controller


def fav_route(app):
   
    @app.route('/user/fav', methods=['GET'])
    def get_fav():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_fav()

    @app.route('/user/fav/<int:id_user>', methods=['GET'])
    def get_user_fav(id_user):  # el id se pasa como param de la funcion
       return Controller.get_user_fav(id_user) # el id se pasa como param de la funcion

    @app.route('/user/fav', methods=['POST'])
    def add_fav():
        body = request.get_json()
        resultado = Controller.add_fav(body)
        return resultado

    @app.route('/user/fav/<int:id>', methods=['DELETE'])
    def delete_single_fav(id):
        return Controller.delete_single_fav(id)

    @app.route('/user/fav/user/<int:id_user>', methods=['DELETE'])
    def delete_all_fav(id_user):
        resultado = Controller.delete_all_fav(id_user)
        return resultado
