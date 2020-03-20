from enum import Enum


class Var(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    NIVEL_LOGS = 'NIVEL_LOGS'
    DIRECTORIO_LOGS = 'DIRECTORIO_LOGS'
    NOMBRE_LOG_PREDEFINIDO = 'NOMBRE_LOG_PREDEFINIDO'
    NOMBRE_LOG_REST = 'NOMBRE_LOG_REST'
    GENERADOR_PDF_HOST = 'GENERADOR_PDF_HOST'
    TAIGA_HOST = 'TAIGA_HOST'
    API_TAIGA_TAREAS = 'API_TAIGA_TAREAS'
    API_TAIGA_SUBTAREAS = 'API_TAIGA_SUBTAREAS'
    DIRECTORIO_ARCHIVO_CONFIG = 'DIRECTORIO_ARCHIVO_CONFIG'
    NOMBRE_ARCHIVO_CONFIG = 'NOMBRE_ARCHIVO_CONFIG'
    EMAIL_ENVIADOR = 'EMAIL_ENVIADOR'
    EMAIL_PASS = 'EMAIL_PASS'


_predefinidas = {
    'VERSION': 'python',
    'PYTHON_HOST': 'localhost',
    'PYTHON_PORT': 5000,
    'NIVEL_LOGS': 'INFO',
    'DIRECTORIO_LOGS': 'resources/logs/',
    'NOMBRE_LOG_PREDEFINIDO': 'app',
    'NOMBRE_LOG_REST': 'rest',
    'GENERADOR_PDF_HOST': 'http://localhost:5001',
    'TAIGA_HOST': 'https://taiga.leafnoise.io/',
    'API_TAIGA_TAREAS': 'api/v1/userstories/csv?uuid=',
    'API_TAIGA_SUBTAREAS': 'api/v1/tasks/csv?uuid=',
    'DIRECTORIO_ARCHIVO_CONFIG': 'resources/configs/',
    'NOMBRE_ARCHIVO_CONFIG': 'taiga-reportes.json',
    'EMAIL_ENVIADOR': 'brian.lobo@moorea.io',
    'EMAIL_PASS': '$leafnoise%'
}

_no_mostrar = []
