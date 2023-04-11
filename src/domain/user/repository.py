from models.index import db, User
from domain.fav.repository import delete_all_fav #el import de la funcion para borrar favoritos
from flask import request, jsonify


def get_users():
    all_users = User.query.all()  # la query va en repositorio

    # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    user_serialized = list(
        map(lambda user: user.serialize_user(), all_users))  # se llama a la funcion que serializa todo excepto el otro mapeo
    return user_serialized


def get_single_user(id):  # el id se pasa como param de la funcion

    user = User.query.get(id)  # la query va en repositorio
    #print (user)
    #para llamar al id se llama a la clase user, metodo query.get pasandole el id como param
    return user


def create_user(data):

    user = User(data['user_name'],  # Agrega el nombre del user
                data['password'], # se agregan los campos del usuario
                data['name'],
                data['last_name'],
                data['email']
                )
    db.session.add(user) #se crea en bd
    db.session.commit()

    return user.serialize() 


def modify_user(id):
    user = User.query.get(id)  # la query va en repositorio
    if user is None:
        return user
    else:
        data = request.get_json()  # este data es el body del postman
        user.user_name = data['user_name']
        user.password = data['password']
        user.name = data['name']
        user.last_name = data['last_name']
        user.email = data['email']
        db.session.commit()

    return user.serialize_user()


def delete_user(id):
    

    user = User.query.get(id)  # la query va en repositorio
    if user is None:  # si el usuario viene vacio
        return user  # retorno la variable como none
    else:
        delete_all_fav(user.id) #se borran los favoritos antes de borrar el propio usuario, para poder hacer esto hay que importarlo arriba
        db.session.delete(user)
        db.session.commit()

    return user
