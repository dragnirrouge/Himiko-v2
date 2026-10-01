import os
import requests
from flask import Flask, Response, redirect, request

app = Flask(__name__)

CLIENT_KEY = os.environ.get("TIKTOK_CLIENT_KEY", "awe4qdszex15zqtl")
CLIENT_SECRET = os.environ.get("TIKTOK_CLIENT_SECRET", "NTH6yAsNFPcHZMQH0UnVxw0m1lNkl746")
REDIRECT_URI = "https://himiko-v2-3.onrender.com/tiktok/callback"
CODE_VERIF = "DLlI4pm5NGE3Twd85kP8cBNjcmKSQF9"

# --- 1. VERIFICATION TIKTOK (garde ton vert) ---
@app.route(f'/tiktok{CODE_VERIF}.txt', methods=['GET', 'HEAD'])
@app.route(f'/tiktok{CODE_VERIF}', methods=['GET', 'HEAD'])
def tiktok_exact():
    return Response(f"tiktok-developers-site-verification={CODE_VERIF}", mimetype='text/plain')

@app.route('/tiktok<intoken>.txt', methods=['GET', 'HEAD'])
@app.route('/tiktok<intoken>', methods=['GET', 'HEAD'])
def tiktok_any(intoken):
    token = intoken.replace('.txt','').strip()
    return Response(f"tiktok-developers-site-verification={token}", mimetype='text/plain')

# --- 2. PAGE D'ACCUEIL AVEC BOUTON LOGIN ---
@app.route('/')
def home():
    return f'''
    <h1>HIMIKO V2 - Connect TikTok</h1>
    <p>Client Key: {CLIENT_KEY[:6]}...</p>
    <a href="/tiktok/login" style="background:black;color:white;padding:15px 30px;text-decoration:none;border-radius:10px;">Login with TikTok</a>
    <br><br>
    <a href="/terms">Terms</a> | <a href="/privacy">Privacy</a>
    '''

@app.route('/terms')
def terms(): return "Terms of Service - Personal use only"
@app.route('/privacy')
def privacy(): return "Privacy Policy - No data shared"

# --- 3. LOGIN ---
@app.route('/tiktok/login')
def login():
    auth_url = (
        f"https://www.tiktok.com/v2/auth/authorize/"
        f"?client_key={CLIENT_KEY}"
        f"&scope=user.info.basic,video.upload,video.publish"
        f"&response_type=code"
        f"&redirect_uri={REDIRECT_URI}"
        f"&state=himiko123"
    )
    return redirect(auth_url)

# --- 4. CALLBACK - RECUPERE LE TOKEN ---
@app.route('/tiktok/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return f"Erreur, pas de code: {request.args}"

    # Echange code contre token
    url = "https://open.tiktokapis.com/v2/oauth/token/"
    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI
    }
    r = requests.post(url, data=data)
    result = r.json()
    
    # Affiche le token pour que tu le copies
    return f"""
    <h1>Connecté !</h1>
    <p>Copie ce résultat et envoie-le moi :</p>
    <pre>{result}</pre>
    <p>Si tu vois access_token, Himiko est connectée à TikTok !</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
