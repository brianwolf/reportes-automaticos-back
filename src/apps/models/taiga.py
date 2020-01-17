from typing import List
from uuid import UUID


class Filtros(object):
    def __init__(self,
                 proyectos: List[str] = [],
                 personas: List[str] = [],
                 estados: List[str] = [],
                 prioridades: List[str] = [],
                 campos_mostrados: List[str] = []):
        self.proyectos = proyectos
        self.personas = personas
        self.estados = estados
        self.prioridades = prioridades
        self.campos_mostrados = campos_mostrados

    def to_dict(self):
        return {
            'proyectos': self.proyectos,
            'personas': self.personas,
            'estados': self.estados,
            'prioridades': self.prioridades,
            'campos_mostrados': self.campos_mostrados
        }

    @staticmethod
    def from_dict(d: dict):
        return Filtros(**d)


class ReportesConfig(object):
    def __init__(self, nombre: str, cron: str, filtros: Filtros,
                 uuid: UUID):
        self.nombre = nombre
        self.cron = cron
        self.filtros = filtros
        self.uuid = uuid

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'cron': self.cron,
            'filtros': self.filtros,
            'uuid': self.uuid
        }

    @staticmethod
    def from_dict(d: dict):
        instancia = ReportesConfig(**d)
        instancia.filtros = Filtros.from_dict(d['filtros'])
        return instancia
