from git import Repo

_USER = 'BrianLobo'
_TOKEN = 'YL31-ZfbcHK3PM4qb6AL'
_URL = f'https://{_USER}:{_TOKEN}@github.com/name/repo.git master'
_DIR = 'repo/'

Repo.clone_from()
