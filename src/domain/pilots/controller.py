# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.pilots.repository as Repository
import handle_response as Response

def get_pilots():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_pilots()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 

def add_pilots(data):

    resultado = Repository.add_pilots(data)
    if resultado is None:
        return Response.response_error('piloto duplicado', 400)
    else:
        return Response.response_ok(resultado)

def delete_single_pilot(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a valid number", 404)

    resultado = Repository.delete_single_pilot(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok("pilot deleted") #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)

def delete_all_pilots(id_starship):
    #print(id_starship)
    if not isinstance(id_starship, int):
        return Response.response_error("Id not found", 404)
    
    resultado = Repository.delete_all_pilots(id_starship)

    return Response.response_ok("all pilots were deleted")