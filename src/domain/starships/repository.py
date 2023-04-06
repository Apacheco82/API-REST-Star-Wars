from models.index import db, Starship
from flask import request, jsonify


def get_starships():
    all_starships = Starship.query.all() #la query va en repositorio

        # starship_serialized = [starship.serialize() for starship in all_starship] array comprehension
    starship_serialized = list(
            map(lambda starship: starship.serialize(), all_starships)) #se llama a la funcion que serializa
    return starship_serialized

def get_single_starship(id):  # el id se pasa como param de la funcion

    starship = Starship.query.get(id)#la query va en repositorio
   # print (starship)
        # para llamar al id se llama a la clase starship, metodo query.get pasandole el id como param
    return starship

def create_starship(data):

    starship = Starship(name=data['name'],
                        model=data['model'],
                        manufacturer=data['manufacturer'],
                        starship_class=data['starship_class'],
                        cost_in_credits=data['cost_in_credits'],
                        length=data['length'],
                        crew=data['crew'],
                        passengers=data['passengers'],
                        max_atmosphering_speed=data['max_atmosphering_speed'],
                        hyperdrive_rating=data['hyperdrive_rating'],
                        mglt=data['mglt'],
                        cargo_capacity=data['cargo_capacity'],
                        consumables=data['consumables'])
    db.session.add(starship)
    db.session.commit()

    return starship.serialize()
        
def modify_starship(id):
    starship = Starship.query.get(id) #la query va en repositorio
    if starship is None:
        return starship
    else:
        data = request.get_json()
        starship.name = data['name']
        starship.model = data['model']
        starship.manufacturer = data['manufacturer']
        starship.starship_class = data['diameter']
        starship.cost_in_credits = data['cost_in_credits']
        starship.length = data['length']
        starship.crew = data['crew']
        starship.passengers = data['passengers']
        starship.max_atmosphering_speed = data['max_atmosphering_speed']
        starship.cargo_capacity = data['cargo_capacity']
        starship.consumables = data['consumables']
        starship.hyperdrive_rating = data['hyperdrive_rating']
        starship.mglt = data['mglt']
        starship.pilots = data['pilots']
        db.session.commit()

    return starship.serialize()      

def delete_starship(id):
        starship = Starship.query.get(id) #la query va en repositorio
        if starship is None: #si el usuario viene vacio
            return starship #retorno la variable como none
        else:
            db.session.delete(starship)
            db.session.commit()

        return starship