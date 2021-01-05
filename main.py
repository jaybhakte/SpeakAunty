import pyttsx3
Dost = pyttsx3.init()
speech = input("Say Something: ")
Dost.say(speech)
Dost.runAndWait()