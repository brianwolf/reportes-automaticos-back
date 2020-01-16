from apps.configs.loggers import get_logger
from apps.models.errores import AppException
from flask import Blueprint, jsonify, request

error_handler_bp = Blueprint('handlers', __name__)

logger = get_logger()


@error_handler_bp.app_errorhandler(Exception)
def handle_exception(e):
    get_logger().exception(str(e))
    return '', 500


@error_handler_bp.app_errorhandler(AppException)
def handle_business_exception(ae: AppException):
    return ae.respuesta_json()
