from models.db import db

class User(db.Model):

    # Definimos las db.Columnas de la tabla Planet
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    fav = db.relationship("Fav", back_populates= "user")

    def __repr__(self):
        return  '%r' % self.user_name #para las relaciones, en lugar de mostrar el id

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
           # "fav" : list(map(lambda fav :fav.fav_serialize(), self.fav )) #mapeo para que se muestren los favoritos de cada usuario, se hace otra funcion serialize de fav para no devolver un bucle infinito
        }