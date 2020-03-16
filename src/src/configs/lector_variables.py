import os
from src.configs.variables import _predefinidas, _no_mostrar, Var


def get(variable: Var) -> str:
    '''
    Obtiene el valor de la variable de entorno correspondiente, en caso de no obtenerla, 
    la saca del archivo de configuracion
    '''
    valor_de_diccionario = _predefinidas.get(variable.value)
    return os.environ.get(variable.value, valor_de_diccionario)


def variables_cargadas() -> dict:
    '''
    Devuelve el mapa de variables con sus valores instanciados y filtrados por la lista de no mostrados
    '''
    return [
        get(clave) for clave in Var.__dict__.keys()
        if clave.value not in _no_mostrar
    ]
