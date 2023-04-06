# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.starships.repository as Repository
import handle_response as Response

def get_starships():
    resultado = Repository.get_starships()
    return Response.response_ok(resultado)

def get_single_starship(id):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase starship, metodo query.get pasandole el id como param
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404) #no va a pasar por esta validación porque le estamos diciendo que traiga un id de tipo int en route

    resultado = Repository.get_single_starship(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok(resultado.serialize()) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 
            
    else:
        return Response.response_error("Id not found", 404)

def create_starship(data):
    # aqui van a ir las validaciones
    
    #validaciones para las naves, si se me ocurre alguna

    resultado = Repository.create_starship(data) # se llama a la funcion de creacion de usuarios de repository

    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response

def modify_starship(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    resultado = Repository.modify_starship(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)

def delete_starship(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a number", 404)
    resultado = Repository.delete_starship(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok("Starship deleted") #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)