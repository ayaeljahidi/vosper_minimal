import whisper
from vosk import Model, KaldiRecognizer, SetLogLevel
import wave, os, sys, json

SetLogLevel(-1)

AUDIO_FILE = sys.argv[1] if len(sys.argv) > 1 else "test.wav"

if not os.path.exists(AUDIO_FILE):
    print(f"Fichier introuvable : {AUDIO_FILE}")
    exit(1)

print(f"\n Fichier : {AUDIO_FILE}\n")

print("Whisper (transcription precise):")
model_w = whisper.load_model("base.en")
result  = model_w.transcribe(AUDIO_FILE, fp16=False)
print(f"  -> {result['text'].strip()}\n")

print("Vosk (detection voix seulement):")
model_v = Model(f"{os.getcwd()}/models/vosk/small")
wf  = wave.open(AUDIO_FILE, "rb")
rec = KaldiRecognizer(model_v, wf.getframerate())
while True:
    data = wf.readframes(4096)
    if not data: break
    if rec.AcceptWaveform(data):
        r = json.loads(rec.Result())
        if r.get("text"): print(f"  -> {r['text']}")
final = json.loads(rec.FinalResult())
if final.get("text"): print(f"  -> {final['text']}")

print("\n Termine !")
