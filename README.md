# SlickMercy

TG: SlickMercy 

## Hackeo de cámaras Hikvision en Android usando Termux

### Termux 
1. Descarga Termux desde F-Droid (es importante obtenerlo de esta app).

### Instalación 
Ejecuta los siguientes comandos en Termux en el orden indicado para evitar errores. Copia y pega uno por uno.

```bash
termux-setup-storage

pkg install python

pkg install python-pip

pkg install git

pkg update && pkg upgrade

pip install colorama

pip install aiohttp

pip install art

pip install pycryptodome

cd storage/downloads

git clone https://github.com/SlickxMercy/SlickMercy
```

### Ejecución de los códigos 
Una vez que hayas terminado de ejecutar los comandos anteriores, sigue las instrucciones a continuación para acceder a la carpeta de descargas.

1. Ingresa a la carpeta de descargas utilizando los siguientes comandos:

```bash
ls     # Para ver las carpetas
cd     # Para abrir la carpeta

# Comúnmente, la carpeta de descargas se abre con este comando:
cd storage/download

ls     # Para ver las carpetas
cd SlickMercy     # Para entrar a la carpeta
```

2. Dentro de la carpeta, encontrarás los scripts. El primero que debes ejecutar es `HostSlick.py`, que se utiliza para escanear el rango de direcciones IP (puedes obtener las IPs buscando "Hikvision" en shodan.io).

```bash
python HostSlick.py
```

Este script escanea puertos y genera una lista de hosts. Para su ejecución, debes ingresar la IP inicial (por ejemplo, 187.140.0.0) y la IP final (por ejemplo, 187.140.250.250). Una vez ingresadas, el escaneo comenzará.

3. El segundo script que debes ejecutar es `ScanSlick.py`. Este script escanea la lista de direcciones IP almacenadas en el archivo llamado `host.txt` y verifica las credenciales. Cuando se encuentra un acceso válido, se guardan capturas de pantalla en la carpeta llamada `pics`. En el nombre de la imagen, encontrarás la IP, el usuario y la contraseña.

```bash
python ScanSlick.py
```

### Actualización 
El script `vulnerabilidad.py` comprueba las cámaras que presentan una vulnerabilidad y obtiene la contraseña de la cámara. guarda las snapshot es la carpeta VDB
