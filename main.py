import os, json, random
from flask import Flask, request, Response
from gtts import gTTS
from moviepy.editor import ColorClip, AudioFileClip

app = Flask(__name__)

# --- VERIFICATION TIKTOK OFFICIELLE ---
@app.route('/tiktokDLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9.txt')
def tiktok_verify_txt():
    return Response("tiktok-developers-site-verification=DLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9", mimetype='text/plain')

@app.route('/tiktokDLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9')
def tiktok_verify():
    return Response("tiktok-developers-site-verification=DLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9", mimetype='text/plain')

@app.route('/terms')
def terms():
    return "Terms of Service for Himiko V2 - Personal use app for managing my own TikTok content @histoire.courte038 @histoire.courte35. No public users."

@app.route('/privacy')
def privacy():
    return "Privacy Policy for Himiko V2 - This app does not collect data from other users. Only for personal account management."

@app.route('/tiktok/callback')
def tiktok_callback():
    code = request.args.get('code')
    return f"TikTok Callback OK - code: {code}. You can now close this window."

@app.route('/')
def home():
    return "HIMIKO V2 FR en ligne - Anti-doublon actif + TikTok Verified OK"

# --- GENERATEUR CINE ---
HISTOIRES_BASE = [
    "POV : Tu découvres que ton meilleur ami t'a menti depuis 3 ans et tu trouves la preuve aujourd'hui",
    "L'astuce que les tiktokeurs à 1M d'abonnés ne veulent pas que tu saches pour percer",
    "Je viens de tester le filtre qui révèle qui t'aime en secret, le résultat m'a choquée",
    "3 phrases qui font tomber n'importe qui amoureux selon la psychologie",
    "Histoire vraie : J'ai retrouvé mon ex à Brazzaville après 5 ans, voilà ce qui s'est passé",
    "Tu fais cette erreur tous les jours et c'est pour ça que tu n'avances pas",
]

HISTORIQUE_FILE = "historique.json"
