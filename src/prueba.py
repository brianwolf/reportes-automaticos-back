from apps.utils.git_util import clonar_repo_git

_REPO_PATH = '/home/brian/Descargas/pruebas/'

_REPO_GIT_URL = 'https://github.com/brianwolf/prueba.git'
_REPO_GIT_USER = 'brianwolf'
_REPO_GIT_PASS = '5cd8d70b68c87bb3c905b247d64f17456232efa8'


repo = clonar_repo_git(_REPO_PATH, _REPO_GIT_URL,
                       _REPO_GIT_USER, _REPO_GIT_PASS)


print(repo.working_dir)
