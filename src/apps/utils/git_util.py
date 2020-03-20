import os
import re
from shutil import rmtree

from git import Git, Repo


def _borrar_carpeta_si_existe(ruta: str):
    '''
    Borra la carpeta en caso de que ya exista
    '''
    if os.path.exists(ruta):
        rmtree(ruta)


def _obtener_nombre_repo(url: str) -> str:
    '''
    Obtiene el nombre del repositorio de la url, es basicamente
    la parte que termina en .../nombre_proyecto.git
    '''
    m = re.search(r'[^\/]+(\.git)', url)
    return m.group(0).replace('.git', '')


def clonar_repo_git(ruta: str, url: str, usuario: str, contrasenia: str) -> Repo:
    '''
    Clona un repo desde git y lo guarda en un directorio
    '''
    url_repo = url.replace('https://', '')
    url_git_final = f'https://{usuario}:{contrasenia}@{url_repo}'

    nombre_repo = _obtener_nombre_repo(url)
    ruta_repo_final = os.path.join(ruta, nombre_repo)

    _borrar_carpeta_si_existe(ruta_repo_final)

    return Repo.clone_from(url_git_final, ruta_repo_final)
