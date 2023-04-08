# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.fav.repository as Repository
import handle_response as Response

def get_fav():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_fav()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 

def planet_fav(data):
    resultado = Repository.planet_fav(data) # se llama a la funcion de creacion de usuarios de repository
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response


def people_fav(id):
    pass

def starship_fav(id):
    pass

def delete_single_fav(id):
    pass

def delete_all_fav():
    pass