import os
import re
from shutil import rmtree

from git import Git, Repo

_REPO_PATH = '/home/brian/Descargas/pruebas/'

_REPO_GIT_URL = 'https://github.com/brianwolf/prueba.git'
_REPO_GIT_USER = 'brianwolf'
_REPO_GIT_PASS = '5cd8d70b68c87bb3c905b247d64f17456232efa8'


def _borrar_carpeta_si_existe(ruta: str):
    '''
    '''
    if os.path.exists(ruta):
        rmtree(ruta)


def _obtener_nombre_repo(url: str) -> str:
    '''
    '''
    m = re.search(r'[^\/]+(\.git)', url)
    return m.group(0).replace('.git', '')


def clonar_repo_git(ruta: str, url: str, usuario: str, contrasenia: str) -> Repo:
    '''
    '''
    url_repo = url.replace('https://', '')
    url_git_final = f'https://{usuario}:{contrasenia}@{url_repo}'

    nombre_repo = _obtener_nombre_repo(url)
    ruta_repo_final = os.path.join(ruta, nombre_repo)

    _borrar_carpeta_si_existe(ruta_repo_final)

    return Repo.clone_from(url_git_final, ruta_repo_final)


repo = clonar_repo_git(_REPO_PATH, _REPO_GIT_URL,
                       _REPO_GIT_USER, _REPO_GIT_PASS)


print(repo.working_dir)
