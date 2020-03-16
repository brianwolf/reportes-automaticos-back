from io import BytesIO
from uuid import UUID

from flask import Blueprint, jsonify, request, send_file

import src.services.taiga.taiga_scheduler_service as taiga_scheduler_service
import src.services.taiga.taiga_service as taiga_service
from src.models.taiga import Filtros, ReportesConfig

blue_print = Blueprint('taiga', __name__, url_prefix='/api/v1/taiga')


@blue_print.route('/csv/tareas/<uuid>/json', methods=['GET'])
def obtener_tareas_json(uuid: UUID):

    diccionario = taiga_service.descargar_csv_tareas_diccionario(uuid)
    return jsonify(diccionario)


@blue_print.route('/csv/subtareas/<uuid>/json', methods=['GET'])
def obtener_subtareas_json(uuid: UUID):

    diccionario = taiga_service.descargar_csv_sub_tareas_diccionario(uuid)
    return jsonify(diccionario)


@blue_print.route(
    '/csv/tareas/<uuid_tareas>/subtareas/<uuid_subtareas>/reporte',
    methods=['POST'])
def obtener_reporte_tareas_y_subtareas(uuid_tareas: UUID,
                                       uuid_subtareas: UUID):

    filtros = Filtros.from_dict(request.get_json())
    diccionario = taiga_service.generar_reporte_proyectos_json(
        uuid_tareas, uuid_subtareas, filtros)

    return jsonify(diccionario)
