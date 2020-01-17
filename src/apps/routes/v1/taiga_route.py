from io import BytesIO
from uuid import UUID

from flask import Blueprint, jsonify, request, send_file

import apps.configs.variables as var
import apps.services.taiga.taiga_service as taiga_service
from apps.models.taiga import Filtros

blue_print = Blueprint('taiga', __name__, url_prefix='/api/v1/taiga')


@blue_print.route('/csv/tareas/<uuid>', methods=['GET'])
def obtener_csv_taiga(uuid=UUID):

    nombre_csv = 'tareas.csv'
    contenido_csv = taiga_service.descargar_csv_tareas(uuid)

    return send_file(BytesIO(contenido_csv),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=nombre_csv)


@blue_print.route('/csv/tareas/<uuid>/json', methods=['GET'])
def obtener_csv_taiga_json(uuid=UUID):

    diccionario = taiga_service.descargar_csv_tareas_diccionario(uuid)
    return jsonify(diccionario)


@blue_print.route('/csv/tareas/<uuid>/reporte', methods=['POST'])
def generar_reporte_json(uuid=UUID):

    json = request.get_json()
    filtros = Filtros(**json)

    diccionario = taiga_service.generar_reporte_json(uuid, filtros)
    return jsonify(diccionario)
