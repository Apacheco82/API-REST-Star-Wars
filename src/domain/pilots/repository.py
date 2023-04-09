from models.index import db, Pilots
from flask import request, jsonify


def get_pilots():
    all_pilots = Pilots.query.all()  # la query va en repositorio
    # pilots_serialized = [pilots.serialize() for pilots in all_pilots] array comprehension
    pilots_serialized = list(
        map(lambda pilots: pilots.serialize(), all_pilots))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return pilots_serialized

def get_single_pilot():
    pass

def add_pilots():
    pass

def delete_single_pilot():
    pass

def delete_all_pilots():
    pass