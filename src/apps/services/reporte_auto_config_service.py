import json
from typing import Dict, List

import apps.configs.variables as var
from apps.models.tareas import ReportesConfig

_NOMBRE_ARCHIVO_CONFIG = var.get('NOMBRE_ARCHIVO_CONFIG')

lista_configs = obtener_json_config()


def guardar_json_config(lista_configs: List[ReportesConfig]):
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    contenido = json.dump(lista_configs)

    with open(_NOMBRE_ARCHIVO_CONFIG, 'w+') as archivo_python:
        archivo_python.write(contenido)


def obtener_json_config() -> List[ReportesConfig]:
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    with open(directorio + nombre, 'r') as archivo:
        json_config = json.load(archivo)

    return [ReportesConfig(**config) for config in json_config]
