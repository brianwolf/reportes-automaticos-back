import json
import os
import shutil
from typing import Dict, List
from uuid import uuid4

import apps.configs.variables as var
from apps.configs.loggers import get_logger
from apps.models.taiga import ReportesConfig

_NOMBRE_ARCHIVO_CONFIG = var.get('NOMBRE_ARCHIVO_CONFIG')
_DIRECTORIO_ARCHIVO_CONFIG = var.get('DIRECTORIO_ARCHIVO_CONFIG')


def guardar_json_config(lista_configs: List[ReportesConfig]):
    '''
    Obtine el json guardado con la configuracion autormatica de los reportes
    '''
    contenido = json.dump(lista_configs)

    if not os.path.exists(_DIRECTORIO_ARCHIVO_CONFIG):
        os.makedirs(_DIRECTORIO_ARCHIVO_CONFIG, exist_ok=True)

    ruta_completa = _DIRECTORIO_ARCHIVO_CONFIG + _NOMBRE_ARCHIVO_CONFIG
    with open(ruta_completa, 'w+') as archivo_python:
        archivo_python.write(contenido)


def obtener_json_config() -> List[ReportesConfig]:
    '''
    Obtine el json guardado con la configuracion automatica de los reportes
    '''
    try:
        ruta_completa = _DIRECTORIO_ARCHIVO_CONFIG + _NOMBRE_ARCHIVO_CONFIG

        if not os.path.exists(ruta_completa):
            mensaje = f'No se encontro el archivo de configuracion en \"{ruta_completa}\"'
            get_logger().info(mensaje)
            return []

        with open(ruta_completa, 'r') as archivo:
            json_config = json.load(archivo)

        return [ReportesConfig.from_dict(config) for config in json_config]

    except Exception as e:
        get_logger().error(str(e))
        return []


def actualizar_json_config(lista_configs: List[ReportesConfig]):
    '''
    Actualiza el json guardado con la configuracion automatica de los reportes
    '''
    if os.path.exists(_DIRECTORIO_ARCHIVO_CONFIG):
        shutil.rmtree(_DIRECTORIO_ARCHIVO_CONFIG)

    guardar_json_config(lista_configs)
