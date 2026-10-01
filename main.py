import os
from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/tiktokDLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9.txt')
def verify_txt():
    return Response("tiktok-developers-site-verification=DLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9", mimetype='text/plain')

@app.route('/tiktokDLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9')
def verify():
    return Response("tiktok-developers-site-verification=DLlJi4pm5NQE3Twd85kP8cBNjcmKSOF9", mimetype='text/plain')

@app.route('/terms')
def terms():
    return "Terms of Service for Himiko V2"

@app.route('/privacy')
def privacy():
    return "Privacy Policy for Himiko V2 - personal use only"

@app.route('/')
def home():
    return "HIMIKO V2 VERIFIED OK"

@app.route('/tiktok/callback')
def callback():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
