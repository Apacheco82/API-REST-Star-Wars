from models.index import db, Fav
from flask import request, jsonify


def get_fav():
    all_fav = Fav.query.all()  # la query va en repositorio
    # fav_serialized = [fav.serialize() for fav in all_fav] array comprehension
    fav_serialized = list(
        map(lambda fav: fav.fav_serialize(), all_fav))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return fav_serialized


def add_fav(data):
    busqueda = Fav.query.filter_by(id_user=data['id_user'], id_planet=data['id_planet'],
                                   id_people=data['id_people'], id_starship=data['id_starship']).all()
    # print(busqueda) si existe uno o mas registros con estos filtros devuelve [<fav2>], si no existe devuelve []
    if busqueda:
        return None
    else:
        fav = Fav(data['id_user'], data['id_planet'], data['id_people'], data['id_starship'])
        db.session.add(fav)
        db.session.commit()
        return fav.fav_serialize()


def delete_single_fav(id):
    fav = Fav.query.get(id)  # la query va en repositorio
    if fav is None:  # si el usuario viene vacio
        return fav  # retorno la variable como none
    else:
        db.session.delete(fav)
        db.session.commit()
    return fav


def delete_all_fav(id_user):
    Fav.query.filter_by(id_user=id_user).delete()
    db.session.commit()
