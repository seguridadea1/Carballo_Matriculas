import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from concurrent.futures import ThreadPoolExecutor
from util import ahora, extension, borrar, base_64, crearToken
from peticiones import traza, call_sessionKey

# Variables susceptibles de ser modificadas
path = "./lpr"
userNonce = "46B303DEAF57847B06961FE1"
userKey = "8f7c88cfbbd0cf0f3507baf1558da39ec8471bfe9bb68315cf13c8dfd28959f4"
tokenLargo = "46B303DEAF57847B06961FE1:1709221264:c3b6dad3512f24eb214d2e09ed6a3f0f9c3201fe19fa1101b0e3265093489c3d"
max_hilos=5

# Colecciones para formatear
colores = {"White": 'Blanco', "Red": 'Rojo', "Green": 'Verde', "Gray": 'Gris', "Black": 'Negro', "Yellow": 'Amarillo', "Blue": 'Azul'}
tipos_vehiculo = {"Truck": 'Camión', "Bus": 'Autobús', "Car": 'Coche', "SUV": 'SUV',"Van": 'Furgoneta'}

def process_file(event):
    
    print("Se ha creado un archivo en " + event.src_path)
    time.sleep(10)
    if extension(event.src_path) == ".jpg":
    
        # Extraer información del evento
        v2 = os.path.basename(event.src_path)
        element = v2.split('_')
    
        # Inicializar y formatear variables
        camara = "15019CARBALLOTRAFFIK" + (element[0])[-1]
        matricula = element[1]
        color = colores.get(element[2], element[2])
        tipo_vehiculo = tipos_vehiculo.get(element[3], element[3])
        imagen_Base64 = base_64(event.src_path)
        print(f"Datos modificados a español: Cámara: {camara}, Matrícula: {matricula}, Color: {color}, Tipo de Vehículo: {tipo_vehiculo}")
        
        # Gestionamos borrado de archivos
        print(borrar(event.src_path))
        # Mandamos traza
        tokenLogin = crearToken(userNonce, userKey)
        sessionKey = call_sessionKey(tokenLogin)
        
        respuesta = traza(sessionKey, camara, color, tipo_vehiculo, matricula, ahora(), imagen_Base64)
        print("Traza : "+ matricula + respuesta)
        
    # Solo se analizan .jpg
    else:
        print("El archivo generado no es una imagen")

def on_created(event):
    
    executor.submit(process_file, event)

if __name__ == "__main__":
    # Configuración del observador
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    # Usamos ThreadPoolExecutor para manejar concurrencia
    with ThreadPoolExecutor(max_workers=max_hilos) as executor:
        try:
            print("Monitor Activo")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("Finalizado")
        observer.join()
