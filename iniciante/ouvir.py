#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from datetime import datetime
from pytz import timezone

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='pt-br')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga Algo!")
        audio = r.listen(source)

    # Speech recogniti  on using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("Você disse: " + data)
    except sr.UnknownValueError:
        print("Google O reconhecimento de fala não conseguiu entender o áudio")
    except sr.RequestError as e:
        print("Não foi possível solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))

    return data

def jarvis(data):

    if "ola" in data:
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

        speak("Eu vou bem!")
        speak("Hoje é")
        speak(data_e_hora_sao_paulo_em_texto)

    if "Como vai você?" in data:
        speak("Eu vou ben!")

    if "Que horas são" in data:
        speak(ctime())

    if "Onde fica" in data:
        data = data.split(" ")
        location = data[2]
        speak("Espere Paula, eu vou te mostrar onde " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
time.sleep(2)
speak("Olá Paula Rutzen, o que posso fazer por você?")
while 1:
    data = recordAudio()
    jarvis(data)
