# video-analitica

# Proyecto de Docker

Este proyecto proporciona un entorno basado en contenedores utilizando Docker. A continuación se describen los pasos para instalar Docker Desktop, construir la imagen y ejecutar el contenedor.

## Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado en tu sistema.
  - Docker Desktop está disponible para macOS, Windows y Linux.
- Conocimientos básicos de uso de la línea de comandos.

## Instalación de Docker Desktop

### En macOS

1. Descarga Docker Desktop desde el [sitio oficial](https://www.docker.com/products/docker-desktop).
2. Abre el archivo `.dmg` descargado y sigue las instrucciones para completar la instalación.
3. Una vez instalado, abre Docker Desktop desde el Launchpad.

### En Windows

1. Descarga Docker Desktop desde el [sitio oficial](https://www.docker.com/products/docker-desktop).
2. Ejecuta el instalador descargado y sigue las instrucciones.
3. Reinicia tu máquina después de la instalación.
4. Una vez reiniciado, abre Docker Desktop desde el menú de inicio.

### En Linux

1. Abre una terminal y ejecuta los siguientes comandos para instalar Docker:

   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

2. Verifica la instalación con el siguiente comando:

   ```bash
   sudo docker --version
   ```

## Construcción de la Imagen Docker

1. Clona este repositorio:

   ```bash
   git clone https://github.com/oportunamastervic/video-analitica.git
   cd tu_repositorio
   ```

2. Construye la imagen Docker usando el siguiente comando:

   ```bash
   docker build -t object_detection .
   ```

   - `object_detection` es el nombre que deseas darle a tu imagen Docker.
   - El punto `.` indica que el `Dockerfile` está en el directorio actual.

## Ejecución del Contenedor

Una vez que hayas construido la imagen, puedes ejecutar el contenedor con:

```bash
docker run -d -p 8080:80 --name nombre_contenedor object_detection
```
