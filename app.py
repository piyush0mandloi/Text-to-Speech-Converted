from flask import Flask, request, jsonify, render_template
import pyttsx3
import os

app=Flask(__name__)


def text_to_speech(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1.0)  # Volume 0-1

    engine.save_to_file(text, 'static/output.mp3')
    engine.runAndWait()
    return 'static/output.mp3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "No text provided!"}), 400
    audio_path = text_to_speech(text)
    return jsonify({"audio_url": f"/{audio_path}"})

@app.route('/favicon.ico')
def favicon():
    return "",204

if __name__ == '__main__':
    app.run(debug=True)