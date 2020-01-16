from uuid import UUID

import apps.configs.variables as var
from apps.configs.loggers import get_logger
from apps.models.errores import AppException
from apps.models.modelos import Modelo


def guardar(modelo: Modelo) -> UUID:
    '''
    Ejemplo de guardado
    '''
    id_generada = UUID()
    return id_generada


def buscar(id: UUID) -> Modelo:
    '''
    Ejemplo busqueda
    '''
    return Modelo('modelo')
