from flask import request, jsonify
from models.index import db, Pilots
import domain.pilots.controller as Controller

def pilots_route(app):

    @app.route('/starships/pilots', methods=['GET'])
    def get_pilots():
        #aqui se retorna el resultado de controller por si quieres hacer validaciones
        return Controller.get_pilots()

    @app.route('/starships/pilots', methods=['POST'])
    def add_pilots():
        body = request.get_json()
        resultado = Controller.add_pilots(body)
        return resultado

    @app.route('/starships/pilots/<int:id_starship>/<int:id_people>', methods=['DELETE'])
    def delete_single_pilot(id_starship, id_people):
        return Controller.delete_single_pilot(id_starship, id_people)

    @app.route('/starships/pilots/starship/<int:id_starship>', methods=['DELETE'])
    def delete_all_pilots(id_starship):
        resultado = Controller.delete_all_pilots(id_starship)
        return resultado


