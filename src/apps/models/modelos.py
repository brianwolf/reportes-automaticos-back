import base64
from datetime import datetime
from uuid import UUID, uuid4

import apps.configs.variables as var


class Modelo(object):
    def __init__(self,
                 nombre,
                 archivos: list = [],
                 id: UUID = uuid4(),
                 fecha_creacion=datetime.now()):
        self.nombre = nombre
        self.archivos = archivos
        self.id = id
        self.fecha_creacion = fecha_creacion

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'archivos': [archivo.to_dict() for archivo in self.archivos],
            'id': str(self.id),
            'fecha_creacion': str(self.fecha_creacion)
        }
