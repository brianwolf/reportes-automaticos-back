# CIRCLECI

Ejemplo de arquitectura de un proyecto usando **python**, **circleci** y **docker**

![alt text](img/python.png)
![alt text](img/circleci.png)
![alt text](img/docker.svg)

## REQUERIMIENTOS

* **Python 3.7**
* **Docker**

## EJECUCION

### PYTHON

* Crear un virtualenv normalmente para python
* Con el virtualenv activado ejecutar **python main.py**

### DOCKER

* Pararse en la ruta raiz del proyecto con docker instalado y funcionando
* Ejecutar el script `./scripts/docker/run.sh`
* Para pararlo ejecutar el script `./scripts/docker/stop.sh`

Los parametros del script `./scripts/docker/ambiente.sh` y las variables de ambiente del archivo *config/ambiente.env*

## CONFIGURACION

* Dentro de la carpeta **config** se encuentran los archivos de variables de ambiente para levantar el docker
* En los scripts **ambiente.sh** encontrados dentro de la carpeta scripts se modifican las variables para sus scripts 

## PAGINAS

[Docker python 3.7 apine](https://hub.docker.com/_/python)
