from models.db import db

class Fav(db.Model):

    # Definimos las db.Columnas de la tabla Planet
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="fav")
    id_planet = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="fav")
    id_people = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship("People", back_populates="fav")
    id_starship = db.Column(db.Integer, db.ForeignKey("starship.id"))
    starship = db.relationship("Starship", back_populates= "fav")

    def __repr__(self):
        return  '%r' % self.id #para las relaciones, en lugar de mostrar el id

    def serialize(self):
        return {
            "id": self.id,
            "user" : self.user,
            "id_user" : self.id_user,
            "id_planet" : self.id_planet,
            "id_people" : self.id_people
        }
    def fav_serialize(self):
        return {
            "id_user" : self.id_user,
            "id_people" : self.id_people,
            "id_planet" : self.id_planet
        }