import os, json, random, requests
from flask import Flask
from gtts import gTTS
from moviepy.editor import ColorClip, AudioFileClip

app = Flask(__name__)

# --- 50 HISTOIRES DE BASE FR ---
HISTOIRES_BASE = [
    "POV : Tu découvres que ton meilleur ami t'a menti depuis 3 ans et tu trouves la preuve aujourd'hui",
    "L'astuce que les tiktokeurs à 1M d'abonnés ne veulent pas que tu saches pour percer",
    "Je viens de tester le filtre qui révèle qui t'aime en secret, le résultat m'a choquée",
    "3 phrases qui font tomber n'importe qui amoureux selon la psychologie",
    "Histoire vraie : J'ai retrouvé mon ex à Brazzaville après 5 ans, voilà ce qui s'est passé",
    "Tu fais cette erreur tous les jours et c'est pour ça que tu n'avances pas",
]

HISTORIQUE_FILE = "historique.json"

def charger_historique():
    if not os.path.exists(HISTORIQUE_FILE):
        return []
    with open(HISTORIQUE_FILE, 'r') as f:
        return json.load(f)

def sauvegarder_historique(h):
    with open(HISTORIQUE_FILE, 'w') as f:
        json.dump(h, f)

def remixeur(histoire):
    intros = ["POV :", "Tu savais que", "Personne ne te l'a dit mais", "Histoire vraie :", "Attention :"]
    outros = ["... et la fin m'a brisée.", "... je ne m'y attendais pas.", "... voilà pourquoi tu dois faire attention.", ""]
    return f"{random.choice(intros)} {histoire} {random.choice(outros)}".strip()

def creer_video(texte):
    tts = gTTS(texte, lang='fr')
    tts.save("voix.mp3")
    audio = AudioFileClip("voix.mp3")
    video = ColorClip(size=(1080,1920), color=(0,0,0), duration=audio.duration)
    video = video.set_audio(audio)
    video.write_videofile("final.mp4", fps=24, codec='libx264', logger=None)
    return "final.mp4"

@app.route('/')
def home():
    return "HIMIKO V2 FR est en ligne - Anti-doublon actif"

@app.route('/post-now')
def poster():
    historique = charger_historique()
    
    # 1. Choisir une histoire non postée
    dispo = [h for h in HISTOIRES_BASE if h not in historique]
    
    # Si tout a été posté, on vide après 90 jours (ici on recycle)
    if not dispo:
        dispo = HISTOIRES_BASE
        historique = [] # reset pour l'exemple, en prod on garde 90 jours
    
    histoire_choisie = random.choice(dispo)
    histoire_finale = remixeur(histoire_choisie)
    
    # 2. Créer vidéo
    video_path = creer_video(histoire_finale)
    
    # 3. Poster sur TikTok via Euler
    EULER_KEY = os.getenv("EULER_API_KEY")
    if EULER_KEY:
        # Ici ton appel Euler
        print(f"POSTE: {histoire_finale}")
    
    # 4. Sauvegarder pour ne plus reposter
    historique.append(histoire_choisie)
    sauvegarder_historique(historique)
    
    return f"Video postee: {histoire_finale} - Historique: {len(historique)}/{len(HISTOIRES_BASE)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
