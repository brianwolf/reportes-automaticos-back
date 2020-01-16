from typing import List


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
