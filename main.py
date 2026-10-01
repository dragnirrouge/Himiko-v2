from flask import Flask
import threading
import os
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"HIMIKO V2 ACTIVE - {datetime.now()} - Brazzaville GMT+1 - OK"

def himiko_loop():
    print("HIMIKO demarree - attente scheduler...")
    # Importe ton ancien code ici
    try:
        # Si tu as un fichier scheduler.py ou bot.py
        import main_old 
    except:
        while True:
            print(f"[{datetime.now()}] HIMIKO en vie - heartbeat")
            time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=himiko_loop, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
