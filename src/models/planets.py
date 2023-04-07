from models.db import db

class Planet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),unique=True, nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    people = db.relationship("People") #no ponemos backpopulates porque no vamos a administrarlo en esta tabla
    fav = db.relationship("Fav", back_populates="planet") #"planet" hace referencia al campo planet de la tabla Fav

    def __repr__(self):
        return  '%r' % self.name #para las relaciones, en lugar de mostrar el id


    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population
        }