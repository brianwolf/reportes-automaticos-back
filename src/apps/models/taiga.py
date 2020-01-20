from typing import List
from uuid import UUID


class FiltrosAbstracto(object):
    def __init__(self,
                 personas: List[str] = [],
                 estados: List[str] = [],
                 campos_mostrados: List[str] = []):
        self.personas = personas
        self.estados = estados
        self.campos_mostrados = campos_mostrados

    def to_dict(self):
        return {
            'personas': self.personas,
            'estados': self.estados,
            'campos_mostrados': self.campos_mostrados
        }


class FiltrosTareas(FiltrosAbstracto):
    def __init__(self,
                 proyectos: List[str] = [],
                 personas: List[str] = [],
                 estados: List[str] = [],
                 prioridades: List[str] = [],
                 campos_mostrados: List[str] = []):
        super().__init__(personas, estados, campos_mostrados)
        self.proyectos = proyectos
        self.prioridades = prioridades

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'proyectos': self.proyectos,
            'prioridades': self.prioridades
        })
        return d

    @staticmethod
    def from_dict(d: dict):
        return FiltrosTareas(**d)


class FiltrosSubTareas(FiltrosAbstracto):
    def __init__(self,
                 personas: List[str] = [],
                 estados: List[str] = [],
                 campos_mostrados: List[str] = []):
        super().__init__(personas, estados, campos_mostrados)

    def to_dict(self):
        return super().to_dict()

    @staticmethod
    def from_dict(d: dict):
        return FiltrosSubTareas(**d)


class Filtros(object):
    def __init__(self,
                 tareas: FiltrosTareas,
                 subtareas: FiltrosSubTareas):
        self.tareas = tareas
        self.subtareas = subtareas

    def to_dict(self):
        return {
            'tareas': self.tareas.to_dict(),
            'subtareas': self.subtareas.to_dict()
        }

    @staticmethod
    def from_dict(d: dict):
        tareas = FiltrosTareas.from_dict(d['tareas'])
        subtareas = FiltrosSubTareas.from_dict(d['subtareas'])
        return Filtros(tareas, subtareas)


class EmailTaiga(object):
    def __init__(self, destinatarios: List[str], copiados: List[str]):
        self.destinatarios = destinatarios
        self.copiados = copiados

    def to_dict(self):
        return {'destinatarios': self.destinatarios, 'copiados': self.copiados}

    @staticmethod
    def from_dict(d: dict):
        return EmailTaiga(**d)


class ReportesConfig(object):
    def __init__(self, nombre: str, cron: str, filtros: Filtros,
                 uuid_tareas: UUID, uuid_sub_tareas: UUID, url_generar_reporte: str,
                 email_taiga: EmailTaiga):
        self.nombre = nombre
        self.cron = cron
        self.filtros = filtros
        self.uuid_tareas = uuid_tareas
        self.uuid_sub_tareas = uuid_sub_tareas
        self.url_generar_reporte = url_generar_reporte
        self.email_taiga = email_taiga

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'cron': self.cron,
            'filtros': self.filtros.to_dict(),
            'uuid_tareas': self.uuid_tareas,
            'uuid_sub_tareas': self.uuid_sub_tareas,
            'url_generar_reporte': self.url_generar_reporte,
            'email_taiga': self.email_taiga.to_dict()
        }

    @staticmethod
    def from_dict(d: dict):
        instancia = ReportesConfig(**d)
        instancia.filtros = Filtros.from_dict(d['filtros'])
        instancia.email_taiga = EmailTaiga.from_dict(d['email_taiga'])
        return instancia
