from models.db import db

class Pilots(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    current = db.Column(db.Boolean(), unique=False, nullable=False)
    id_people = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship("People", back_populates="pilots") #"pilots" hace referencia al campo pilots de la tabla People
    id_starship = db.Column(db.Integer, db.ForeignKey("starship.id"))
    starship = db.relationship("Starship", back_populates="pilots") #"pilots" hace referencia al campo pilots de la tabla Starship

    def __repr__(self):
        return  '%r' % self.id_people #para las relaciones, en lugar de mostrar el id

    def serialize(self):
        return {
            #"id": self.id,
            "current" : self.current, 
            "id_people" : self.id_people,
            #"id_starship" : self.id_starship   
        }