from models.db import db

class Fav(db.Model):

    # Definimos las db.Columnas de la tabla Planet
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="fav") #"fav" hace referencia al campo fav de la tabla User
    id_planet = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="fav") #"fav" hace referencia al campo fav de la tabla Planet
    id_people = db.Column(db.Integer, db.ForeignKey("people.id"))
    people = db.relationship("People", back_populates="fav") #"fav" hace referencia al campo fav de la tabla People
    id_starship = db.Column(db.Integer, db.ForeignKey("starship.id"))
    starship = db.relationship("Starship", back_populates= "fav") #"fav" hace referencia al campo fav de la tabla Starship


    def serialize(self):
        return {
            "id": self.id,
            "user" : self.user,
            "id_user" : self.id_user,
            "id_planet" : self.id_planet,
            "id_people" : self.id_people,
            "id_starship" : self.id_starship
        }
    def fav_serialize(self): #se crea esta funcion para usarla en el mapeo de user para devolver los datos de los favoritos del usuario
        return { #se omite el user para no volver a serializar cada vez los favoritos del user y que no sea recursivo
            #"id_user" : self.id_user,
            "id_people" : self.id_people,
            "id_planet" : self.id_planet,
            "id_starship" : self.id_starship

        }