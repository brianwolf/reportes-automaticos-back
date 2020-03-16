from flask import Blueprint, jsonify, request

import src.configs.lector_variables as var
from src.configs.variables import Var, _predefinidas
from src.configs.loggers import get_logger
from src.models.errores import AppException

blue_print = Blueprint('errors', __name__, url_prefix='')

logger = get_logger()


@blue_print.route('/variables')
def variables():
    respuesta = {}
    for clave in _predefinidas.keys():
        respuesta[clave] = var.get(Var(clave))

    return jsonify(respuesta)


@blue_print.route('/error')
def error():
    raise AppException('PRUEBA', 'Rompimos todo vieja!')


@blue_print.route('/')
def vivo():
    logger.info("VIVO")
    respuesta = {"estado": "vivo"}
    return jsonify(respuesta)
