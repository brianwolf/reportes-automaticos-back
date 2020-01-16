from typing import List


class ReportesConfig(object):
    def __init__(self, nombre: str, cron: str, filtros: Filtros,
                 url_datos: str):
        self.nombre = nombre
        self.cron = cron
        self.filtros = filtros
        self.url_datos = url_datos

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'cron': self.cron,
            'filtros': self.filtros,
            'url_datos': self.url_datos
        }


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
