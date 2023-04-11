from models.index import db, Pilots
from flask import request, jsonify



def get_pilots():
    all_pilots = Pilots.query.all()  # la query va en repositorio
    #print(all_pilots)
    # pilots_serialized = [pilots.serialize() for pilots in all_pilots] array comprehension
    pilots_serialized = list(
        map(lambda pilots: pilots.serialize(), all_pilots))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return pilots_serialized


def add_pilots(data):
    busqueda = Pilots.query.filter_by(id_people=data['id_people'], id_starship=data['id_starship']).all()
    # print(busqueda) si existe uno o mas registros con estos filtros devuelve [<fav2>], si no existe devuelve []
    if busqueda:
        return None
    else:
        pilot = Pilots(data['id_people'], data['id_starship'])
        db.session.add(pilot)
        db.session.commit()
        return pilot.serialize()


def delete_single_pilot(id):
    
    pilot = Pilots.query.get(id)  # la query va en repositorio
    if pilot is None:  # si el usuario viene vacio
        return pilot  # retorno la variable como none
    else:
        db.session.delete(pilot)
        db.session.commit()
    return pilot


def delete_all_pilots(id_starship):
    Pilots.query.filter_by(id_starship=id_starship).delete()
    db.session.commit()
