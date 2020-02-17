
import os
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def cria_audio(audio):
	engine.say(audio)
	engine.runAndWait()

	#tts = gTTS(audio,lang='pt-br')
	#date_string = datetime.now().strftime("%d%m%Y%H%M%S")
	#filename = "voice"+date_string+".mp3"
	#tts.save(filename)
	#playsound(filename)


def ouvir_microfone():
	microfone = sr.Recognizer()
	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		print("Diga alguma coisa: ")
		audio = microfone.listen(source)


	try:
		frase = microfone.recognize_google(audio,language='pt-br')
		print("Você disse: " + frase)

	except sr.UnknownValueError:
		print("Não entendi")

	return frase




audio = ouvir_microfone()
	

if "laboratório" in audio:
	cria_audio("Laboratório 6 está liberado")

if "Lucas" in audio:
	playsound('audios/lucas.mp3')

if "Gregory" in audio:
	playsound('audios/greg1.mp3')

if "folhas" in audio:
	cria_audio("Digite Sua Matrícula")

if "Globo" in audio:
	cria_audio("Olá, irei abrir o Chrome para o Senhor"),
	os.startfile("https://www.globo.com")

if "e-mail" in audio:
	os.startfile("https://gmail.com/")

if "Elder Scrolls" in audio:
	os.startfile("C:\Program Files (x86)\Mr DJ\The Elder Scrolls V Skyrim Legendary Edition\SkyrimLauncher.exe")
	
if "piada" in audio:
	cria_audio("Claro"),
	cria_audio("Tinham duas impressoras:"),
	cria_audio("Uma disse para a outra:"),
	cria_audio("É impressão minha ou essa folha e sua?"),

	


#if "folhas" in audio:
#	matricula = int(input('Matricula: '))
#	cria_audio("Você Disse: " + str(matricula)),
#	cria_audio("Você Possui 10 Impressões")
