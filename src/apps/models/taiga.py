from dataclasses import dataclass, field
from typing import List
from uuid import UUID


@dataclass
class FiltrosAbstracto:
    personas: List[str] = field(default_factory=list)
    estados: List[str] = field(default_factory=list)
    campos_mostrados: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            'personas': self.personas,
            'estados': self.estados,
            'campos_mostrados': self.campos_mostrados
        }


@dataclass
class FiltrosTareas(FiltrosAbstracto):
    proyectos: List[str] = field(default_factory=list)
    personas: List[str] = field(default_factory=list)
    estados: List[str] = field(default_factory=list)
    prioridades: List[str] = field(default_factory=list)
    campos_mostrados: List[str] = field(default_factory=list)

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


@dataclass
class FiltrosSubTareas(FiltrosAbstracto):
    personas: List[str] = field(default_factory=list)
    estados: List[str] = field(default_factory=list)
    campos_mostrados: List[str] = field(default_factory=list)

    def to_dict(self):
        return super().to_dict()

    @staticmethod
    def from_dict(d: dict):
        return FiltrosSubTareas(**d)


@dataclass
class Filtros:
    tareas: FiltrosTareas
    subtareas: FiltrosSubTareas

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


@dataclass
class EmailTaiga:
    destinatarios: List[str]
    copiados: List[str]

    def to_dict(self):
        return {'destinatarios': self.destinatarios, 'copiados': self.copiados}

    @staticmethod
    def from_dict(d: dict):
        return EmailTaiga(**d)


@dataclass
class ReportesConfig:
    nombre: str
    cron: str
    filtros: Filtros
    uuid_tareas: UUID
    uuid_sub_tareas: UUID
    url_generar_reporte: str
    email_taiga: EmailTaiga

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
