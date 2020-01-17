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


class EmailTaiga(object):
    def __init__(self,
                 destinatarios: List[str],
                 copiados: List[str]):
        self.destinatarios = destinatarios
        self.copiados = copiados

    def to_dict(self):
        return {
            'destinatarios': self.destinatarios,
            'copiados': self.copiados
        }

    @staticmethod
    def from_dict(d: dict):
        return EmailTaiga(**d)


class ReportesConfig(object):
    def __init__(self, nombre: str, cron: str, filtros: Filtros,
                 uuid_csv: UUID, url_generar_reporte: str, email_taiga: EmailTaiga):
        self.nombre = nombre
        self.cron = cron
        self.filtros = filtros
        self.uuid_csv = uuid_csv
        self.url_generar_reporte = url_generar_reporte
        self.email_taiga = email_taiga

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'cron': self.cron,
            'filtros': self.filtros.to_dict(),
            'uuid_csv': self.uuid_csv,
            'url_generar_reporte': self.url_generar_reporte,
            'email_taiga': self.email_taiga.to_dict()
        }

    @staticmethod
    def from_dict(d: dict):
        instancia = ReportesConfig(**d)
        instancia.filtros = Filtros.from_dict(d['filtros'])
        instancia.email_taiga = EmailTaiga.from_dict(d['email_taiga'])
        return instancia
