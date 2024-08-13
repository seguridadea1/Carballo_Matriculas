import hashlib
import time
from datetime import datetime
import base64
import os

limite_archivos=20

def crearToken(user_nonce, user_key):
    try:
        timestamp = generate_timestamp()
        hash_value = generate_hex_encoded(str(timestamp) + user_key)
        token = f"{user_nonce}:{timestamp}:{hash_value}"
        return token
    except Exception as ex:
        return str(ex)

def generate_hex_encoded(text):
    hex_encoded = text.encode('utf-8')
    hashed = hashlib.sha256(hex_encoded).digest()
    return bytes_to_hex(hashed)

def generate_timestamp():
    return int(time.time() * 1000)

def bytes_to_hex(hash_bytes):
    return ''.join('{:02x}'.format(byte) for byte in hash_bytes)

def ahora():
    fechaPlana= datetime.now()
    fecha=fechaPlana.strftime('%Y-%m-%dT%H:%M:%S' + 'Z')
    return fecha

def base_64(ruta):
    
        try:
            with open(ruta, "rb") as image_file:
                image_binary = image_file.read()
                base64_image = base64.b64encode(image_binary).decode('utf-8')
                return base64_image
            
        except FileNotFoundError:
            print(f"File '{ruta}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

def extension(ruta_archivo):
    _, extension=os.path.splitext(ruta_archivo)
    return extension.lower()

def borrar_carpeta(ruta_directorio):

    files = [os.path.join(ruta_directorio, f) for f in os.listdir(ruta_directorio) if os.path.isfile(os.path.join(ruta_directorio, f))]
    files.sort(key=os.path.getmtime, reverse=True)

    files_to_delete = files[limite_archivos:]

    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Eliminado: {file}")
        except Exception as e:
            print(f"No se pudo eliminar {file}. Error: {e}")

def borrar (ruta_evento):

    try:
        os.remove(ruta_evento)
        print(f"Eliminado: "+ruta_evento)
    
    except Exception as e:
        print(f"No se pudo eliminar " + ruta_evento + ". Error: " + e)