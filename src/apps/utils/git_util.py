import os
import re
from dataclasses import dataclass
from shutil import rmtree

from git import Git, Repo

from apps.configs.lector_variables import get
from apps.configs.variables import Var


@dataclass
class GitConfig:
    url_repo: str
    usuario: str
    contrasenia: str
    ruta_clonado: str = get(Var.CARPETA_TMP)

    @staticmethod
    def from_dict(d: dict) -> 'GitConfig':
        url_repo = d['url_repo']
        usuario = d['usuario']
        contrasenia = d['contrasenia']
        ruta_clonado = d.get('ruta_clonado', get(Var.CARPETA_TMP))
        return GitConfig(url_repo, usuario, contrasenia, ruta_clonado)

    def to_dict(self):
        return self.__dict__()


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


def clonar_repo_git(config: GitConfig) -> Repo:
    '''
    Clona un repo desde git y lo guarda en un directorio
    '''
    url_repo = config.url_repo.replace('https://', '')
    url_git_final = f'https://{config.usuario}:{config.contrasenia}@{url_repo}'

    nombre_repo = _obtener_nombre_repo(config.url_repo)
    ruta_repo_final = os.path.join(config.ruta_clonado, nombre_repo)

    _borrar_carpeta_si_existe(ruta_repo_final)

    return Repo.clone_from(url_git_final, ruta_repo_final)


def pushear_a_master(repo: Repo, mensaje_commit: str):
    '''
    Pushea a master todos los cambios hechos en la carpeta del repo,
    es similar a ejecutar:\n
    git add .\n
    git commit -m "{mensage_commit}"\n
    git push
    '''
    repo.index.add(repo.working_dir + '/*')
    repo.index.commit(mensaje_commit)
    repo.remote().push()
