from io import BytesIO
from uuid import UUID

from flask import Blueprint, jsonify, request, send_file

import apps.configs.variables as var
import apps.services.taiga_service as taiga_service
from apps.models.tareas import Filtros

blue_print = Blueprint('taiga', __name__, url_prefix='/api/v1/taiga')


@blue_print.route('/csv/tareas/', methods=['GET'])
def obtener_csv_taiga():

    nombre_csv = 'tareas.csv'
    contenido_csv = taiga_service.descargar_csv_tareas()

    return send_file(BytesIO(contenido_csv),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=nombre_csv)


@blue_print.route('/csv/tareas/json', methods=['GET'])
def obtener_csv_taiga_json_predefinido():

    diccionario = taiga_service.descargar_csv_tareas_diccionario()
    return jsonify(diccionario)


@blue_print.route('/reportes/json', methods=['POST'])
def generar_reporte_json():

    json = request.get_json()
    filtros = Filtros(**json)

    diccionario = taiga_service.generar_reporte_json(filtros)
    return jsonify(diccionario)
