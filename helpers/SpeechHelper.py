import pyttsx3

class SpeechHelper:
    def __init__(self):
        self.engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        self.engine.setProperty('voice', en_voice_id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)

    def speakText(self,text):
        self.engine.say(text)
        self.engine.runAndWait()