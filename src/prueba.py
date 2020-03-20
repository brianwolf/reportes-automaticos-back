import os
import re

from git import Git, Repo

_REPO_PATH = '/home/brian/Descargas/pruebas/'

_REPO_GIT_URL = 'https://github.com/brianwolf/python-script.git'
_REPO_GIT_USER = 'brianwolf'
_REPO_GIT_PASS = '5cd8d70b68c87bb3c905b247d64f17456232efa8'


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

    return Repo.clone_from(url_git_final, ruta_repo_final)
