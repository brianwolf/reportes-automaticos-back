import json
import os

from flask import Flask, jsonify

import apps.configs.variables as var
import apps.services.taiga_scheduler_service as taiga_scheduler_service
from apps.configs.error_handlers import error_handler_bp
from apps.services.taiga_reportes_config_service import guardar_json_config
from apps.utils.carga_dinamica_blue_prints import registrar_blue_prints

PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))

app = Flask(__name__)
app.register_blueprint(error_handler_bp)

registrar_blue_prints(app, 'apps/routes')

taiga_scheduler_service.iniciar()


# import apps.schedulers.prueba2 as prueba2

if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
