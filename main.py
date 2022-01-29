import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
   try:
       with sr.Microphone() as source:
          print('listening...')
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          check = command.lower()
          if 'Thaponsak' in command:
              command = command.replace('Thaponsak', '')
              print(command)
   except:
       pass
   return command

def run_Thaponsak():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing some song' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i already have girlfriend')
    elif 'are you single' in command:
        talk('i have my girlfriend name yin')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

while True:
     run_Thaponsak()