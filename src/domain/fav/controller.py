# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.fav.repository as Repository
import handle_response as Response

def get_fav():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_fav()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 

def get_user_fav(id_user):  # el id se pasa como param de la funcion
        # para llamar al id se llama a la clase fav, metodo query.get pasandole el id como param
    if not isinstance(id_user, int):
        return Response.response_error("Id is not a number", 404) #no va a pasar por esta validación porque le estamos diciendo que traiga un id de tipo int en route

    resultado = Repository.get_user_fav(id_user) #usando como param el id 
    if resultado is not None:
        return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 
            
    else:
        return Response.response_error("Id not found", 404)

def add_fav(data):
    if data.get('id_planet') is not None:
        fav = data['id_planet']
    elif data.get('id_people') is not None:
        fav = data['id_people']
    elif data.get('id_starship') is not None:
        fav = data['id_starship']
    else:
        return Response.response_error('Debe proporcionar un solo tipo de favorito', 400)

    if sum(map(lambda x: x is not None, [data.get('id_planet'), data.get('id_people'), data.get('id_starship')])) > 1:
        return Response.response_error('Debe proporcionar solo un tipo de favorito', 400)

    resultado = Repository.add_fav(data)
    if resultado is None:
        return Response.response_error('favorito duplicado', 400)
    else:
        return Response.response_ok(resultado)

def delete_single_fav(id):
    if not isinstance(id, int):
        return Response.response_error("Id is not a valid number", 404)

    resultado = Repository.delete_single_fav(id) #usando como param el id 
    if resultado is not None:
        return Response.response_ok("fav deleted") #se utiliza la variable resultado para pasarla a response y que devuelva un msg  
    else:
        return Response.response_error("Id not found", 404)

def delete_all_fav(id_user):

    if not isinstance(id_user, int):
        return Response.response_error("Id not found", 404)
    
    resultado = Repository.delete_all_fav(id_user)
    return Response.response_ok("all favs were deleted")
