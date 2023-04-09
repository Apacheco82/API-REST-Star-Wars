from models.db import db

class People(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(250))
    homeworld_planet = db.Column(db.Integer, db.ForeignKey("planet.id"))
    Homeworld = db.relationship("Planet", back_populates="people") #el campo del planeta natal
    fav = db.relationship("Fav", back_populates="people")
    pilots = db.relationship("Pilots", back_populates="people")

    def __repr__(self):
        return  '%r' % self.name #para las relaciones, en lugar de mostrar el id

    def __init__(self, name, height, mass, skin_color, eye_color, birth_year, gender, homeworld_planet):
        self.name = name
        self.height = height
        self.mass = mass
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld_planet = homeworld_planet

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld_planet": self.homeworld_planet
        }
