import speech_recognition as sr

r = sr.Recognizer()  # initialize recognizer
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    r.adjust_for_ambient_noise(source, duration=1)
    print("Speak Anything :")
    audio = r.listen(source)  # listen to the source
    try:
        message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(message))

    except:
        print("Sorry could not recognize your voice")