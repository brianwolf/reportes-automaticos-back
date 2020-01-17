from apps.models.taiga import Filtros
from typing import List, Dict
import re

_CLAVE_TAGS = 'tags'
_CLAVE_PERSONAS = 'assigned_to_full_name'
_CLAVE_ESTADOS = 'status'

_PREFIJO_NOMBRE_PROYECTO = '$ '
_PREFIJO_NOMBRE_PRIORIDAD = '- '

_NOMBRE_PROYECTO_VACIO = 'varios'
_NOMBRE_PRIORIDAD_VACIO = 'sin Prioridad'

_REGEX_NOMBRE_PROYECTO = '\$ \w*'
_REGEX_NOMBRE_PRIORIDAD = '\- \w*'


def filtrar(tareas: List[Dict], filtros: Filtros) -> List[Dict]:
    '''
    Filtra las tareas en base a los filtros pasados por parametro
    '''
    tareas = _filtrar_por_clave(tareas, _CLAVE_ESTADOS, filtros.estados)
    tareas = _filtrar_por_clave(tareas, _CLAVE_PERSONAS, filtros.personas)
    tareas = filtrar_por_prioridades(tareas, filtros.prioridades)
    tareas = filtrar_por_proyectos(tareas, filtros.proyectos)

    return tareas


def filtrar_campos_mostrados(tareas: List[Dict],
                             campos_a_mostrar: List[str]) -> List[Dict]:
    '''
    Filtra los campos de la tareas dejando solo los que esten en la lista de campos a mostrar
    '''
    resultado = []
    for tarea in tareas:

        diccionario_aux = {}
        for clave, valor in tarea.items():
            if clave in campos_a_mostrar:
                diccionario_aux[clave] = valor

        resultado.append(diccionario_aux)

    return resultado


def _filtrar_por_clave(tareas: List[Dict], clave: str,
                       filtros: List[str]) -> List[Dict]:
    '''
    Filtra por una clave en especifico que corresponde con el csv que arroja Taiga
    '''
    if not filtros:
        return tareas

    return [tarea for tarea in tareas if tarea[clave] in filtros]


def filtrar_por_proyectos(tareas: List[Dict],
                          proyectos: List[str]) -> List[Dict]:
    '''
    Filtra las tareas dejando solo las que tengan un proyecto incluido en la lista de proyectos
    '''
    if not proyectos:
        return tareas

    return [
        tarea for tarea in tareas
        if _parsear_nombre_proyecto(tarea[_CLAVE_TAGS]) in proyectos
    ]


def filtrar_por_prioridades(tareas: List[Dict],
                            prioridades: List[str]) -> List[Dict]:
    '''
    Filtra las tareas dejando solo las que tengan una prioridad incluida en la lista de prioridades
    '''
    if not prioridades:
        return tareas

    return [
        tarea for tarea in tareas
        if _parsear_nombre_prioridad(tarea[_CLAVE_TAGS]) in prioridades
    ]


def _parsear_nombre_proyecto(valor_tags: str) -> str:
    '''
    Obtiene el nombre del proyecto en base al valor del tag
    '''
    match = re.match(_REGEX_NOMBRE_PROYECTO, valor_tags, re.IGNORECASE)
    if match:
        return match.group(0).replace(_PREFIJO_NOMBRE_PROYECTO, '')

    return _NOMBRE_PROYECTO_VACIO


def _parsear_nombre_prioridad(valor_tags: str) -> str:
    '''
    Obtiene el nombre de la prioridad en base al valor del tag
    '''
    match = re.match(_REGEX_NOMBRE_PRIORIDAD, valor_tags, re.IGNORECASE)
    if match:
        return match.group(0).replace(_PREFIJO_NOMBRE_PRIORIDAD, '')

    return _NOMBRE_PRIORIDAD_VACIO


def agrupar_por_proyectos(tareas: List[Dict]) -> List[Dict]:
    '''
    Agrupa las tareas por los nombres de sus proyectos onvolucrados
    '''
    proyectos_agrupados = []
    for proyecto in _obtener_grupos_proyectos(tareas):

        tareas_proyecto = [
            tarea for tarea in tareas
            if proyecto == _parsear_nombre_proyecto(tarea[_CLAVE_TAGS])
        ]

        proyectos_agrupados.append({proyecto: tareas_proyecto})

    return proyectos_agrupados


def _obtener_grupos_proyectos(tareas: List[Dict]) -> List[Dict]:
    '''
    Obtiene los nombres de los proyectos sin repetir de las tareas
    '''
    grupos = []
    for tarea in tareas:

        nombre_proyecto = _parsear_nombre_proyecto(tarea[_CLAVE_TAGS])
        if not nombre_proyecto in grupos:
            grupos.append(nombre_proyecto)

    return grupos
