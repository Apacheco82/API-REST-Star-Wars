# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.fav.repository as Repository
import handle_response as Response

def get_fav():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_fav()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 


def add_fav(data):
    if data.get('id_planet') is not None:
        favorite_type = 'planet'
        favorite_id = data['id_planet']
    elif data.get('id_people') is not None:
        favorite_type = 'people'
        favorite_id = data['id_people']
    elif data.get('id_starship') is not None:
        favorite_type = 'starship'
        favorite_id = data['id_starship']
    else:
        return Response.response_error('Debe proporcionar un solo tipo de favorito', 400)

    if sum(map(lambda x: x is not None, [data.get('id_planet'), data.get('id_people'), data.get('id_starship')])) > 1:
        return Response.response_error('Debe proporcionar solo un tipo de favorito', 400)

    # Chequeo para evitar la inserción de una combinación de favoritos ya existente
    #if Repository.check_duplicate_favorites(data['id_user'], favorite_type, favorite_id):
     #   return Response.response_error('La combinación de favorito ya existe', 400)

    resultado = Repository.add_fav(data)

    return Response.response_ok(resultado)




def starship_fav(id):
    pass

def delete_single_fav(id):
    pass

def delete_all_fav():
    pass