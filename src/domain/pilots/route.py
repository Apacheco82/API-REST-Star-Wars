from flask import request, jsonify
from models.index import db, Pilots
import domain.pilots.controller as Controller

def pilots_route(app):

    @app.route('/starships/pilots', methods=['GET'])
    def get_pilots():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_pilots()

    @app.route('/starships/pilots/<int:id>', methods=['GET'])
    def get_single_pilot(id):  # el id se pasa como param de la funcion
       return Controller.get_single_pilots(id) # el id se pasa como param de la funcion

    @app.route('/starships/pilots', methods=['POST'])
    def add_pilots():
        body = request.get_json()
        resultado = Controller.add_pilots(body)
        return resultado

    @app.route('/starships/pilots/<int:id>', methods=['DELETE'])
    def delete_single_pilot(id):
        return Controller.delete_single_pilots(id)

    @app.route('/starships/pilots/starships/<int:id_starships>', methods=['DELETE'])
    def delete_all_pilots(id_starships):
        resultado = Controller.delete_all_pilots(id_starships)
        return resultado


