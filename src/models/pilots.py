from models.db import db

class Pilots(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship("People", back_populates="pilots")
    id_starship = db.Column(db.Integer, db.ForeignKey("starship.id"))
    starship = db.relationship("Starship", back_populates="pilots")

    def __repr__(self):
        return  '%r' % self.id_people #para las relaciones, en lugar de mostrar el id

    def serialize(self):
        return {
            "id": self.id, 
            "id_people" : self.id_people,
            "id_starship" : self.id_starship   
        }