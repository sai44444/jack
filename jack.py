from flask import Flask, request, jsonify,render_template
import wave
import vosk
import json


model = vosk.Model(r"C:\\vosk-model-small-en-in-0.4\\vosk-model-small-en-in-0.4")

@app.route("/")
def home():
    return render_template("testeh.html")

@app.route('/process_audio', methods=['POST'])
def process_audio():
    audio_data = request.get_data()
    recognizer = vosk.KaldiRecognizer(model, 16000)
    audio_data1 = json.loads(request.data)['audio']
    print(audio_data1)
    recognizer.AcceptWaveform(audio_data)
    result = json.loads(recognizer.FinalResult())
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
