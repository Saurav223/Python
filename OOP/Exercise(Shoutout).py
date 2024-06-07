import pyttsx3

def speech(texts):
    voice = pyttsx3.init()
    for text in texts:
        voice.say("Shout out to " + text)
    voice.runAndWait()

name = ['Saurav','Ram','Harry','Shandy']
speech(name)

