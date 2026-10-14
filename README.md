# ¿Página de la UNI Caída? 🤖💥

> Script viejo y random para chequear si el sistema de matrícula / SIU de la UNI Managua ya revivió o sigue en el suelo, mandando alerta por Telegram.

```text
       .---.                [ BOT STATUS ]
      /     \                     │
     | () () |  <-- (Bot)         ▼
      \  -  /            .------------------.
     .-'`=-'`-.          | ¿Servidor UNI:   |
    /          \         |   ¿Vivo o Muerto?|
   | |        | |        '------------------'
   | |        | |                 │
   (_|        |_)                 ▼
      |  __  |            .---------------.
      | |  | |            |  _   _ _   _  |
      |_|  |_|            | | | | | \ | | |
     (__)  (__)           | | | | |  \| | |
                          | |_| | | |\  | |
    [ UNI MANAGUA ]       |  \___/|_| \_| |
  .-----------------.     |    [ SIU-UNI ]|
  |  /\     /\   __ |     '---------------'
  | /  \   /  \ [__]|            │
  |/    \_/    \ |  |            ▼
  '-----------------'    ( 404 / 500 / TIMEOUT )
   Líder en Ciencia       "Sigue caída, dormí
     y Tecnología          otro ratito... 😴"
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
