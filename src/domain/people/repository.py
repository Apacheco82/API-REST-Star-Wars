from models.index import db, People
from flask import request, jsonify


def get_people():
    all_people = People.query.all() #la query va en repositorio

        # people_serialized = [people.serialize() for people in all_people] array comprehension
    people_serialized = list(
            map(lambda people: people.serialize(), all_people)) #se llama a la funcion que serializa 
    return people_serialized

def get_single_people(id):  # el id se pasa como param de la funcion

    people = People.query.get(id)#la query va en repositorio
   # print (people)
        # para llamar al id se llama a la clase people, metodo query.get pasandole el id como param
    return people

def create_people(data):

    people = People(name=data['name'],  # Agrega el nombre del planeta
                        height=data['height'],
                        mass=data['mass'],
                        skin_color=data['skin_color'],
                        eye_color=data['eye_color'],
                        birth_year=data['birth_year'],
                        gender=data['gender'],
                        homeworld_planet=data['homeworld_planet'])
    db.session.add(people)
    db.session.commit()

    return people.serialize()
        
def modify_people(id):
    people = People.query.get(id) #la query va en repositorio
    if people is None:
        return people
    else:
        data = request.get_json()
        people.name = data['name']
        people.height = data['height']
        people.mass = data['mass']
        people.skin_color = data['skin_color']
        people.eye_color = data['eye_color']
        people.birth_year = data['birth_year']
        people.gender = data['gender']
        people.homeworld_planet = data['homeworld_planet']
        db.session.commit()

    return people.serialize()      

def delete_people(id):
        people = People.query.get(id) #la query va en repositorio
        if people is None: #si el usuario viene vacio
            return people #retorno la variable como none
        else:
            db.session.delete(people)
            db.session.commit()

        return people