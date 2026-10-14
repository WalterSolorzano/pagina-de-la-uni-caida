# ¿Página de la UNI Caída? 💥

> Script viejo y random para chequear si el sistema de matrícula / SIU de la UNI Managua ya revivió o sigue en el suelo, mandando alerta por Telegram.

```text
    =========================================
          UNIVERSIDAD NACIONAL DE INGENIERIA
                 UNI - MANAGUA
    =========================================

             /\             /\
            /  \   UNI     /  \
           /    \         /    \
          /  /\  \_______/  /\  \
         /  /  \           /  \  \
        /__/    \_________/    \__\
       |                          |
       |  LIDER EN CIENCIA Y TEC. |
       ============================

            [ ESTADO DEL SERVIDOR ]
                       │
                       ▼
           ┌────────────────────────┐
           │   SIU - NOTAS UNI      │
           │  ¿Revivió la página?   │
           └────────────────────────┘
                       │
                       ▼
             HTTP 500 / TIMEOUT
          "Sigue caída... a mimir 😴"
```

---

## 📜 ¿De qué va esto?

Cada temporada de matrícula en la UNI el portal colapsaba. Este script hacía polling a `https://siu.uni.edu.ni/notasuni/Login.aspx` y en cuanto respondía HTTP 200, te avisaba por Telegram para correr antes de que se volvieran a agotar los cupos.

## 🛠️ Requisitos

```bash
pip install -r requirements.txt
```

## 🚀 Uso

Configura tus credenciales en `monitor_telegram.py`:
- `TELEGRAM_TOKEN`
- `TELEGRAM_CHAT_ID`

Y luego ejecútalo:

```bash
python monitor_telegram.py
```
