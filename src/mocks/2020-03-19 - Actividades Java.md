![alt text](https://upload.wikimedia.org/wikipedia/commons/5/55/Phantom_Unit_Logo.jpg)

# Reporte de actividades Java

> Reporte de actividades Java autogenerado a la fecha 2020-03-19



## :open_file_folder: moorea

    
    
### :heavy_check_mark: Agregar firma con huella digital

Agregar la imagen de la huella digital que me viene por parametro en una nueva pagina del pdf (no se si lo busco de digiweb o me viene)
    
        

    
    
### :heavy_check_mark: Migración de estructuras, proyecto moorea

Se realizó la migración del proyecto moorea, que utilizaba una estructura de carpetas anticuada, a un estructura nueva. Además, se realizó refactorización general del código.
    
        
        
* **1) Migración de configuración basada en geters y seters, a una configuración basada en Map** 
        
        
* **2) Migración de clases y dependencias a la nueva estructura de paquetes** 
        
        
* **3) Correcciones necesarias para que el proyecto funcione en la nueva estructura** 
        
        
* **4) Clonación y refactorización de codigo** 
        

    
    
### :heavy_check_mark: Modificar carga de certificados

Modificar la forma en que se cargan los certificados. Actualmente se cargan en b64, modificarlo por carpeta que contenga archivos ".cert"
    
        
        
* **Permitir que los archivos se carguen desde files** 
        
        
* **Permitir que las rutas de los archivos contenedores de los certificados (electrónicos y digitales), sean seteables desde las properties** 
        
        
* **Permitir carga secundaria. En caso de no encontrar la carpeta, se deben cargar a partir de b64** 
        

    



## :open_file_folder: todos

    
    
### :heavy_check_mark: Generar mockeador de servicios

Generar mockeador generico de servicios en python. Se debe poder especificar el path al cual se realizará la consulta, el tipo de petición y el methodo. Además, se deberá poder especificar un response esperado
    
        
        
* **Generar json con la estructura del mock request** 
        
        
* **Investigar como obtener todos los posibles path a partir de la base "/"** 
        
        
* **Generar estructura de objetos para que sea escalable a futuras solicitudes** 
        
        
* **Generar estructura de carpetas donde se almacenarán las configuraciones de la descripción** 
        
        
* **Realizar la carga de mock request a partir de la carga de los archivos de configuración** 
        
        
* **Generar controller que permita refrescar la carga de configuraciones** 
        
        
* **Mapear los responses a los files de las carpetas** 
        

    
    
### :heavy_check_mark: Documentar el código del mockeador

Generar la documentación de los métodos del mockeador. Explicar el funcionamiento y refactorizar en caso de ser necesario.
    
        

    



## :open_file_folder: sadil

    
    
### :heavy_check_mark: Refactor repositorys

Refactorizar repositorys para hacer inserts y updates en las tablas, tanto de Db2 como de Sql, ya que tiene problemas cuando los datos son NULLs. (Aclaración: El problema era Spring)
    
        
        
* **Descartar problema con versiones de base de datos** 
        
        
* **Descartar problema con drivers de base de datos** 
        
        
* **Descartar problema de spring** 
        

    
    
### :heavy_check_mark: Crear controller para testear

Crear controller que permita ejecutar de forma individual y conjunta las funcionalidades de la aplicación para detectar posibles errores en los servicios utilizados.
    
        

    
    
### :heavy_check_mark: Acceso a servidor de digiweb

Pedir acceso desde Jboss al servidor de digiweb para poder subir archivos pdf
    
        

    
    
### :heavy_check_mark: Cambiar método de actualizacón de tablas

Cambiar la forma en que se insertan los datos en las base de datos, tanto db2 como sql. De manera que se inserte de un certificado a la vez, y no todos juntos.
    
        

    
    
### :heavy_check_mark: Informar error en SP de DB2

Informar error en SP de DB2 para guardar certificados, que consulta una tabla errónea.
    
        

    

