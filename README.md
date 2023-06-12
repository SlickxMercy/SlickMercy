# SlickMercy
TG: SlickMercy 

# Hack camaras hikvision (Android)

# Termux 
Descarga termux de F-Droid
(importante)

# instalacion 
ejecuta los siguientes comando en termux por orden para evitar errores 
copien y peguen uno por uno 


termux-setup-storage

pkg install python

pkg install python-pip

pkg install git

pkg update && pkg upgrade

pip install colorama

pip install aiohttp

pip install art

pip install pycryptodome

cd storage/download

git clone https://github.com/SlickxMercy/SlickMercy

# Ejecutar codigos 
cuando termines de ejecutar los comandos anteriores 

entra a la carpeta de descargas, para eso sigue los siguientes comandos

ls (para ver las carpetas)
cd (para abrir la carpeta 

comunmente la carpeta de descargas se abre con este comando 

cd storage/download
ls (para ver las carpetas)
cd SlickMercy (para entrar a la carpeta)

encontraras los scripts, el primero en ejecutar serian HostSlick.py para escanear el rango de ips (las ips la puedes obtener buscando hikvision en shodan.io)

python HostSlick.py
este sirve para escanear puertos y obtener una lista de host (primero debes colocar la ip inicial por ejemplo 187.140.0.0 das enter y colocas la ip final 187.140.250.250 enter y empezara a scanear)

segundo script 

python ScanSlick.py
sirve para escanear la listas del archivo llamado host.txt y hace comprobaciónes de credenciales, cuando el acceso es correcto se guardan snapshots en la carpeta llamada pics 
en el nombre de la imagen encontras la ip, usuario y contraseña 

# Update 
script vulnerabilidad.py
comprueba camaras que tienen una vulnerabilidad y obtiene la contraseña de la cámara (por ahora no guarda las snapshot de las cámaras)
