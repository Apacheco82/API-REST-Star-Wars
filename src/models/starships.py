from models.db import db


class Starship(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True,nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.String(250), nullable=False)
    mglt = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String(250))
    fav = db.relationship("Fav", back_populates= "starship") #"starship" hace referencia al campo starship de la tabla Fav
    pilots = db.relationship("Pilots", back_populates="starship")# "starship" hace referencia al campo starship de la tabla Pilots



    def __repr__(self):
        return  '%r' % self.name #para las relaciones, en lugar de mostrar el id

    def __init__(self, name, model, manufacturer, starship_class, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, mglt, cargo_capacity, consumables=None):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.starship_class = starship_class
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.mglt = mglt
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables

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



