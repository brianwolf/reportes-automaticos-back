import logging
import os

import apps.configs.lector_variables as var
from apps.configs.variables import Var

DIRECTORIO_LOGS = var.get(Var.DIRECTORIO_LOGS)
NOMBRE_LOG_PREDEFINIDO = var.get(Var.NOMBRE_LOG_PREDEFINIDO)
NIVEL_LOGS = var.get(Var.NIVEL_LOGS)

_loggers = {}


def get_logger(nombre=NOMBRE_LOG_PREDEFINIDO) -> logging.Logger:
    '''
    Devuelve un objeto logger por un nombre, en caso de que no exista lo crea
    '''
    if nombre in _loggers.keys():
        return _loggers[nombre]

    if not os.path.exists(DIRECTORIO_LOGS):
        os.makedirs(DIRECTORIO_LOGS, exist_ok=True)

    logger = logging.getLogger(nombre)
    logger.setLevel(NIVEL_LOGS)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s (%(process)d) - %(levelname)s - %(message)s')

    sh = logging.StreamHandler()
    sh.setLevel(NIVEL_LOGS)
    sh.setFormatter(formatter)

    fh = logging.FileHandler(DIRECTORIO_LOGS + f"{nombre}.log")
    fh.setLevel(NIVEL_LOGS)
    fh.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(fh)

    _loggers[nombre] = logger

    return logger
