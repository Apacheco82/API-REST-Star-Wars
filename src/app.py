"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models.index import db, User, Planet, People, Starship, Fav, Pilots
from admin import setup_admin
from domain.user.route import user_route
from domain.people.route import people_route
from domain.planets.route import planets_route
from domain.fav.route import fav_route
from domain.pilots.route import pilots_route
from domain.starships.route import starships_route





app = Flask(__name__)
app.url_map.strict_slashes = False



db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
user = user_route(app)
people = people_route(app)
planet = planets_route(app)
starship = starships_route(app)
pilot = pilots_route(app)
fav = fav_route(app)



@app.route('/')
def get_all():
    all_planets = Planet.query.all()  # se trae los elementos de la clase
    # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    planet_serialized = list(  # mapeamos los elementos
        map(lambda planet: planet.serialize(), all_planets))  # mapea con una funcion y un iterable (all_planets)
    all_people = People.query.all()
    # people_serialized = [people.serialize() for people in all_people] array comprehension
    people_serialized = list(
        map(lambda people: people.serialize(), all_people))
    all_starships = Starship.query.all()
    # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    starship_serialized = list(
        map(lambda starship: starship.serialize(), all_starships))
    all_users = User.query.all()
    # planet_serialized = [planet.serialize() for planet in all_planets] array comprehension
    user_serialized = list(
        map(lambda user: user.serialize(), all_users))

    response = {
        "result": {
            "planets": planet_serialized,
            "people": people_serialized,
            "starships": starship_serialized,
            "user": user_serialized

        }
    }

    return response, 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
