# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.fav.repository as Repository
import handle_response as Response

def get_fav():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_fav()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 



def planet_fav(data):
    # aqui van a ir las validaciones
    if data['id_planet'] is None or data['id_planet'] == '':
        return Response.response_error('planeta not valid', 400)


    resultado = Repository.planet_fav(data)
    return Response.response_ok(resultado)



def people_fav(id):
    pass

def starship_fav(id):
    pass

def delete_single_fav(id):
    pass

def delete_all_fav():
    pass