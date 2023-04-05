from models.db import db


class Starship(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    mglt = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.Integer)
    fav = db.relationship("Fav", back_populates= "starship")
    pilots = db.relationship("Pilots", back_populates="starship")



    def __repr__(self):
        return  '%r' % self.name #para las relaciones, en lugar de mostrar el id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables, 
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt" : self.mglt,
            "pilots" : list(map(lambda pilots: pilots.serialize(), self.pilots ))
        }

