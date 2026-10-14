import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TELEGRAM_TOKEN = "757009NOLOVEAS"  
TELEGRAM_CHAT_ID = "750067"  
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

URL_UNIVERSIDAD = "https://siu.uni.edu.ni/notasuni/Login.aspx"

def enviar_mensaje_telegram(mensaje):
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
    }
    response = requests.post(TELEGRAM_API_URL, params=params)
    if response.status_code == 200:
        print("Mensaje enviado a Telegram.")
    else:
        print("Error al enviar el mensaje a Telegram.")

def verificar_pagina():
    try:
        response = requests.get(URL_UNIVERSIDAD, verify=False, timeout=10)  # Timeout de 10 segundos
        if response.status_code == 200:
            enviar_mensaje_telegram("¡La página está activa! Ve a matricularte.")
            return True
        else:
            print(f"Página no disponible. Código de estado: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar: {e}")
        return False

start_time = time.time()  
duration = 10 * 60  

while time.time() - start_time < duration:
    if verificar_pagina():
        break  
    time.sleep(60)  

print("El script ha finalizado después de 10 minutos.")
