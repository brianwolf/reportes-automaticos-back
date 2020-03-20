import os

from apps.utils.git_util import clonar_repo_git

_REPO_PATH = '/home/brian/Descargas/pruebas/'

_REPO_GIT_URL = 'https://github.com/brianwolf/prueba.git'
_REPO_GIT_USER = 'brianwolf'
_REPO_GIT_PASS = 'c2868a14e317f3fcf179be183b6fba556e7d135b'


repo = clonar_repo_git(_REPO_PATH, _REPO_GIT_URL,
                       _REPO_GIT_USER, _REPO_GIT_PASS)


# print(repo.heads)

ruta_archivo_nuevo = os.path.join(repo.working_dir, 'archivo.txt')

with open(ruta_archivo_nuevo, 'w') as archivo_nuevo:
    archivo_nuevo.write('hola mundo :)!')

repo.index.add(repo.working_dir + '/*')
repo.index.commit("agego archivo")

repo.remote().push()


from datetime import datetime
print(datetime.now().date())