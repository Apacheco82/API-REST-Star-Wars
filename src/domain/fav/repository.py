from models.index import db, Fav
from flask import request, jsonify


def get_fav():
    all_fav = Fav.query.all()  # la query va en repositorio
    # fav_serialized = [fav.serialize() for fav in all_fav] array comprehension
    fav_serialized = list(
        map(lambda fav: fav.fav_serialize(), all_fav))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return fav_serialized

#crear get fav por usuario id

def planet_fav(data):
    #chequeo para que no exista el id que le pasamos como favorito antes de añadirlo
    fav = Fav(data['id_user'],  # Agrega el nombre del user
                data['id_planet'],
                data['id_people'],
                data['id_starship']
                )
    db.session.add(fav)
    db.session.commit()

    return fav.fav_serialize()

def people_fav(data):
    pass

def starship_fav(data):
    pass

def delete_single_fav(id):
    pass

def delete_all_fav():
    pass