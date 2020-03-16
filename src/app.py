import json
import os

from flask import Flask, jsonify

import src.configs.lector_variables as var
import src.services.taiga.taiga_scheduler_service as taiga_scheduler_service
from src.configs.error_handlers import error_handler_bp
from src.configs.variables import Var
from src.services.taiga.taiga_reportes_config_service import \
    guardar_json_config
from src.utils.carga_dinamica_blue_prints import registrar_blue_prints

PYTHON_HOST = var.get(Var.PYTHON_HOST)
PYTHON_PORT = int(var.get(Var.PYTHON_PORT))

app = Flask(__name__)
app.register_blueprint(error_handler_bp)

registrar_blue_prints(app, 'src/routes')

# taiga_scheduler_service.iniciar_proceso_automatico()

if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
