from models.index import db, Fav
from flask import request, jsonify


def get_fav():
    all_fav = Fav.query.all()  # la query va en repositorio
    # fav_serialized = [fav.serialize() for fav in all_fav] array comprehension
    fav_serialized = list(
        map(lambda fav: fav.fav_serialize(), all_fav))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return fav_serialized



#def check_duplicate_favorites(id_planet, id_people, id_starship, id_user):
 #   return Fav.query.filter_by(id_planet=id_planet, id_people=id_people, id_starship=id_starship, id_user=id_user).first() is not None
    #usa el método query de SQLAlchemy para buscar registros en la tabla Fav que tengan los mismos valores 
    # de id_planet, id_people, id_starship e id_user que los valores proporcionados en la solicitud. 
    # Si encuentra algún registro que coincida, devuelve True; de lo contrario, devuelve False.



def add_fav(data):
    fav = Fav(
        data['id_user'],data['id_planet'],data['id_people'],data['id_starship']
    )

    db.session.add(fav)
    db.session.commit()

    return fav.fav_serialize()


def delete_single_fav(id):
    pass

def delete_all_fav():
    pass