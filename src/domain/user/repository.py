from models.index import db, User
from flask import request, jsonify


def get_users():
    all_users = User.query.all() #la query va en repositorio

        # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    user_serialized = list(
            map(lambda user: user.serialize_user(), all_users)) #se llama a la funcion que serializa todo excepto el otro mapeo
    return user_serialized

def get_single_user(id):  # el id se pasa como param de la funcion

    user = User.query.get(id)#la query va en repositorio
   # print (user)
        # para llamar al id se llama a la clase user, metodo query.get pasandole el id como param
    return user

def create_user(data):

    user = User(user_name=data['user_name'],  # Agrega el nombre del user
                    password=data['password'],
                    name=data['name'],
                    last_name=data['last_name'],
                    email=data['email']
                    )
    db.session.add(user)
    db.session.commit()

    return user.serialize()
        
def modify_user(id):
    user = User.query.get(id) #la query va en repositorio
    if user is None:
        return user
    else:
        data = request.get_json() #este data es el body del postman
        user.user_name = data['user_name']
        user.password = data['password']
        user.name = data['name']
        user.last_name = data['last_name']
        user.email = data['email']
        db.session.commit()

    return user.serialize_user()      

def delete_user(id):
        user = User.query.get(id) #la query va en repositorio
        if user is None: #si el usuario viene vacio
            return user #retorno la variable como none
        else:
            db.session.delete(user)
            db.session.commit()

        return user