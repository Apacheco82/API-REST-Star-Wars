from models.index import db, Planet
from flask import request, jsonify


def get_planets():
    all_planets = Planet.query.all() #la query va en repositorio

        # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    planet_serialized = list(
            map(lambda planet: planet.serialize(), all_planets)) #se llama a la funcion que serializa
    return planet_serialized

def get_single_planet(id):  # el id se pasa como param de la funcion

    planet = Planet.query.get(id)#la query va en repositorio
   # print (planet)
        # para llamar al id se llama a la clase planet, metodo query.get pasandole el id como param
    return planet

def create_planet(data):

    planet = Planet(data['name'],  # Agrega el nombre del planeta
                        data['rotation_period'],
                        data['orbital_period'],
                        data['diameter'],
                        data['climate'],
                        data['gravity'],
                        data['terrain'],
                        data['surface_water'],
                        data['population'])
    db.session.add(planet)
    db.session.commit()

    return planet.serialize()
        
def modify_planet(id):
    planet = Planet.query.get(id) #la query va en repositorio
    if planet is None:
        return planet
    else:
        data = request.get_json()
        planet.name = data['name']
        planet.rotation_period = data['rotation_period']
        planet.orbital_period = data['orbital_period']
        planet.diameter = data['diameter']
        planet.climate = data['climate']
        planet.gravity = data['gravity']
        planet.terrain = data['terrain']
        planet.surface_water = data['surface_water']
        planet.population = data['population']
        db.session.commit()

    return planet.serialize()      

def delete_planet(id):
        planet = Planet.query.get(id) #la query va en repositorio
        if planet is None: #si el usuario viene vacio
            return planet #retorno la variable como none
        else:
            db.session.delete(planet)
            db.session.commit()

        return planet