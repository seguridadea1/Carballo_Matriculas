import requests
import json


#Variables usadas por más de un método
base_url = "http://2.136.61.100:9002"
headers = {'Content-Type': 'application/json'}


def call_sessionKey(tokenLogin):

    endpoint = "/API_SrvTraffik/Login"

    body = {
        "tokenLogin": tokenLogin,
        "tipoServicio": "Trazas"
        }
    
    try :

    
        response = requests.request("POST",base_url + endpoint, headers=headers,data=json.dumps(body))
        
        
        return(response.text)
    
    except Exception as e:

        return "Error: "+str(e)

def traza(sessionKey,nombreCamara,color,tipo_vehiculo,matricula,fechaHora,foto):

    try:
        url = "http://2.136.61.100:9002/API_SrvTraffik/AddTrazas"

        payload = json.dumps({
            "sessionKey": sessionKey,
            "trazas": 
            [
                {  
                    "nombreCamara": nombreCamara,
                    "sentido":"Desconocido",
                    "matricula": matricula,
                    "fechaHora": fechaHora,
                    "color": color,
                    "tipo_vehiculo": tipo_vehiculo,
                    "Foto": foto
                }
            ]})
        
        response = requests.request("POST",url ,headers=headers,data=payload)
        
        return(response.text)
    
    except Exception as e:
        return "Error: "+str(e)


