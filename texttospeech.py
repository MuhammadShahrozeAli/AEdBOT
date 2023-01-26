from gtts import gTTS
from playsound import playsound

text = 'This is in english language'
var = gTTS(text = text)
var.save("eng.mp3")
playsound("eng.mp3")