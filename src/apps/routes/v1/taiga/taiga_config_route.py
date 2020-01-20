import json

from flask import Blueprint, jsonify, request, send_file

import apps.services.taiga.taiga_reportes_config_service as taiga_reportes_config_service
from apps.models.taiga import Filtros, ReportesConfig

blue_print = Blueprint('taiga_configuraciones', __name__,
                       url_prefix='/api/v1/taiga/configs')


@blue_print.route('/reportes', methods=['GET'])
def obtener_taiga_config():

    configs = taiga_reportes_config_service.obtener_json_config()
    return jsonify([config.to_dict() for config in configs])


@blue_print.route('/reportes', methods=['PUT'])
def actualizar_taiga_config():

    lista_diccionarios = request.get_json()
    configs = [ReportesConfig.from_dict(config)
               for config in lista_diccionarios]

    taiga_reportes_config_service.actualizar_json_config(configs)
    return '', 200


@blue_print.route('/reportes', methods=['POST'])
def nueva_taiga_config():

    lista_diccionarios = request.get_json()
    configs = [ReportesConfig.from_dict(config)
               for config in lista_diccionarios]

    taiga_reportes_config_service.guardar_json_config(configs)
    return '', 201
