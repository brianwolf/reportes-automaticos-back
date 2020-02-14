###########################################################
# VARIABLES
###########################################################

AUTH_TOKEN=eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjo0NH0:1irRiH:oUqpBojEsvIlCX14QHJVrpsgCtw
HOST=https://taiga.leafnoise.io
ARCHIVO_RESULTADO=resultado.json


###########################################################
# URLS
###########################################################

# PROYECTOS
# API=/api/v1/projects



# TAREAS DEL PROYECTO
API=/api/v1/search?project=9


# API=/api/v1/userstories


# API=/api/v1/tasks



###########################################################
# PRUEBAS
###########################################################

curl -X GET \
-H "Content-Type: application/json" \
-H "Authorization: Bearer ${AUTH_TOKEN}" \
-s $HOST$API \
> $ARCHIVO_RESULTADO

