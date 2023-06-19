import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as src:
    print("say something...")
    audio = rec.listen(src)
    text = rec.recognize_google(audio)
print(text)