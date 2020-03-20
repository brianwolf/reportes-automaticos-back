from io import BytesIO
from uuid import UUID

from flask import Blueprint, jsonify, request, send_file

import apps.configs.lector_variables as var
import apps.services.taiga.taiga_scheduler_service as taiga_scheduler_service
import apps.services.taiga.taiga_service as taiga_service
from apps.models.taiga import Filtros, ReportesConfig

blue_print = Blueprint('taiga_generador',
                       __name__,
                       url_prefix='/api/v1/taiga/generador')


@blue_print.route('/ejecutar/todos', methods=['GET'])
def generar_todos_los_reportes_manualmente():

    taiga_scheduler_service.generar_todos_los_reportes_manualmente()
    return ''


@blue_print.route('/reportes/tareas/json', methods=['POST'])
def generar_reporte_json():

    json_entrada = request.get_json()

    uuid_tareas = json_entrada['uuid_tareas']
    uuid_subtareas = json_entrada['uuid_subtareas']
    filtros = Filtros.from_dict(json_entrada['filtros'])

    diccionario = taiga_service.generar_reporte_proyectos_json(
        uuid_tareas, uuid_subtareas, filtros)

    return jsonify(diccionario)
