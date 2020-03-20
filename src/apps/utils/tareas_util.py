import re
from typing import Dict, List

from apps.models.taiga import Filtros, FiltrosSubTareas, FiltrosTareas

_CLAVE_TAGS = 'tags'
_CLAVE_PERSONAS = 'assigned_to_full_name'
_CLAVE_ESTADOS = 'status'
_CLAVE_SUB_TAREAS = 'tasks'

_CLAVE_SUB_TAREA_REFERENCIA = 'ref'

_PREFIJO_NOMBRE_PROYECTO = '$ '
_PREFIJO_NOMBRE_PRIORIDAD = '- '

_NOMBRE_PROYECTO_VACIO = 'varios'
_NOMBRE_PRIORIDAD_VACIO = 'sin Prioridad'

_REGEX_NOMBRE_PROYECTO = '\$ \w*'
_REGEX_NOMBRE_PRIORIDAD = '\- \w*'


def agrupar_tareas_con_sub_tareas(tareas: List[Dict], subtareas: List[Dict]) -> dict:
    '''
    Agrupa las subtareas con su tarea correspondiente
    '''
    for tarea in tareas:

        if not tarea[_CLAVE_SUB_TAREAS]:
            continue

        ref_sub_tareas = tarea[_CLAVE_SUB_TAREAS].split(',')

        tarea[_CLAVE_SUB_TAREAS] = [
            _sub_tarea_por_referencia(subtareas, ref_sub_tarea)
            for ref_sub_tarea in ref_sub_tareas
        ]

    return tareas


def _sub_tarea_por_referencia(subtareas: List[Dict], referencia: str) -> dict:
    '''
    Devuelve la sub tarea que corresponde con esa referencia
    '''
    for sub_tarea in subtareas:
        if referencia == sub_tarea[_CLAVE_SUB_TAREA_REFERENCIA]:
            return sub_tarea


def filtrar(tareas: List[Dict], filtros: FiltrosTareas) -> List[Dict]:
    '''
    Filtra las tareas en base a los filtros pasados por parametro
    '''
    tareas = _filtrar_por_clave(tareas, _CLAVE_ESTADOS, filtros.estados)
    tareas = _filtrar_por_clave(tareas, _CLAVE_PERSONAS, filtros.personas)
    tareas = filtrar_por_prioridades(tareas, filtros.prioridades)
    tareas = filtrar_por_proyectos(tareas, filtros.proyectos)

    return tareas


def filtrar_sub_tareas(subtareas: List[Dict], filtros: FiltrosSubTareas) -> List[Dict]:
    '''
    Filtra las subs tareas en base a los filtros pasados por parametro
    '''
    subtareas = _filtrar_por_clave(
        subtareas, _CLAVE_PERSONAS, filtros.estados)
    subtareas = _filtrar_por_clave(
        subtareas, _CLAVE_PERSONAS, filtros.personas)
    return subtareas


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

        proyectos_agrupados.append({
            "nombre": proyecto,
            "tareas": tareas_proyecto
        })

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
