# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.user.repository as Repository
import handle_response as Response


def create_user(data):
    # aqui van a ir las validaciones
    if data['email'] is None or data['email'] == '':
        return Response.response_error('Email not valid', 400)

    if data['user_name'] is None or data['user_name'] == '':
        return Response.response_error('user not valid', 400)

    resultado = Repository.create_user(data) # se llama a la funcion de creacion de usuarios de repository

    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response
