import pyttsx3

engine = pyttsx3.init()
#change the speech rate
rate = engine.getProperty("rate")
engine.setProperty("rate",180)
#change the voice
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
say = "Hey! I am Meghan"
engine.say(say)
engine.runAndWait()