# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.user.repository as Repository
import handle_response as Response

def get_users():
#se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_users()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 

def get_single_user(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase user, metodo query.get pasandole el id como param
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404) #no va a pasar por esta validación porque le estamos diciendo que traiga un id de tipo int en route

    resultado = Repository.get_single_user(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok(resultado.serialize()) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 
            
    else:
        return Response.response_error("Id not found", 404)

def create_user(data):
    # aqui van a ir las validaciones
    if data['email'] is None or data['email'] == '':
        return Response.response_error('Email not valid', 400)

    if data['user_name'] is None or data['user_name'] == '':
        return Response.response_error('user not valid', 400)

    resultado = Repository.create_user(data) # se llama a la funcion de creacion de usuarios de repository

    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response

def modify_user(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    resultado = Repository.modify_user(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)

def delete_user(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    resultado = Repository.delete_user(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok("User deleted") #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)