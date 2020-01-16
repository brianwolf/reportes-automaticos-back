import json
import os

from flask import Flask, jsonify
from apps.configs.error_handlers import error_handler_bp

import apps.configs.variables as var
from apps.utils.carga_dinamica_blue_prints import registrar_blue_prints

PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))

app = Flask(__name__)
app.register_blueprint(error_handler_bp)

registrar_blue_prints(app, 'apps/routes')

if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
