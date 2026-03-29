import urllib.request, zipfile, os, shutil

URL = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
ZIP = "vosk-model-small.zip"
DIR = os.path.join("models", "vosk", "small")

if os.path.exists(DIR):
    print("Modele Vosk deja installe !")
else:
    print("Telechargement du modele Vosk...")
    def progress(count, block, total):
        pct = int(count * block * 100 / total)
        print(f"\r  [{('#'*(pct//2)):<50}] {pct}%", end="", flush=True)
    urllib.request.urlretrieve(URL, ZIP, progress)
    print("\nExtraction...")
    with zipfile.ZipFile(ZIP, "r") as z:
        z.extractall(".")
    os.makedirs(os.path.join("models", "vosk"), exist_ok=True)
    shutil.move("vosk-model-small-en-us-0.15", DIR)
    os.remove(ZIP)
    print("Modele installe !")

print("\nPret ! Lancez : python test_file.py test.wav")
