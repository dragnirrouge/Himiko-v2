import os
import re
from flask import Flask, Response, request
app = Flask(__name__)

# SOLUTION DEFINITIVE : sers TOUS les fichiers tiktok automatiquement
@app.route('/tiktok<path:token>')
def tiktok_verify(token):
    # token peut être DLlI... .txt ou DLlI...
    clean = token.replace('.txt','').replace('/','')
    # enlève tout ce qui n'est pas le code
    clean = re.sub(r'[^A-Za-z0-9]', '', clean)
    content = f"tiktok-developers-site-verification={clean}"
    return Response(content, mimetype='text/plain')

@app.route('/')
def home():
    return "HIMIKO V2 LIVE - tiktok verification OK"

@app.route('/terms')
def terms():
    return "Terms of Service - Himiko V2 personal bot"

@app.route('/privacy')
def privacy():
    return "Privacy Policy - Himiko V2 personal bot"

@app.route('/tiktok/callback')
def callback():
    return "Callback OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
