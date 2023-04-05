from models.index import db, User


def create_user(data):

    user = User(user_name=data['user_name'],  # Agrega el nombre del user
                    password=data['password'],
                    name=data['name'],
                    last_name=data['last_name'],
                    email=data['email']
                    )
    db.session.add(user)
    db.session.commit()

    return user.serialize()
