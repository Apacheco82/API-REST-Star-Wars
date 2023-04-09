from flask import request, jsonify
from models.index import db, Fav
import domain.fav.controller as Controller


def fav_route(app):
   
    @app.route('/user/fav', methods=['GET'])
    def get_fav():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_fav()

    @app.route('/user/fav/<int:id>', methods=['GET'])
    def get_single_fav(id):  # el id se pasa como param de la funcion
       return Controller.get_single_fav(id) # el id se pasa como param de la funcion

    @app.route('/user/fav', methods=['POST'])
    def planet_fav():
        body = request.get_json()
        return Controller.planet_fav(body), 201
    
    @app.route('/user/fav', methods=['POST'])
    def people_fav(id):
        body = request.get_json()
        return Controller.people_fav(body), 201

    @app.route('/user/fav', methods=['POST'])
    def starship_fav(id):
        body = request.get_json()
        return Controller.starship_fav(body), 201

    @app.route('/user/fav/<int:id>', methods=['DELETE'])
    def delete_single_fav(id):
        return Controller.delete_single_fav(id)

    @app.route('/user/fav' , methods=['DELETE'])
    def delete_all_fav():
        return Controller.delete_all_fav()