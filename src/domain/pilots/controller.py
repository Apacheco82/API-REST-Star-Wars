# se importan todas las funciones del repository, si se hace asi vienen todas y no una a una
import domain.pilots.repository as Repository
import handle_response as Response

def get_pilots():
    #se pasa la funcion por aqui por si se quieren meter validaciones
    resultado = Repository.get_pilots()
    return Response.response_ok(resultado) #se utiliza la variable resultado para pasarla a response y que devuelva un msg 

def get_single_pilot():
    pass

def add_pilots():
    pass

def delete_single_pilot():
    pass

def delete_all_pilots():
    pass