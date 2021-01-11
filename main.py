import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
sofia = pyttsx3.init()
voices= sofia.getProperty('voices')
sofia.setProperty('voice', voices[1].id)

def talk(text):
    sofia.say(text)
    sofia.runAndWait()

def input_command():
    try:
        with sr.Microphone() as sound_source:

            print('say something...')
            voice = listener.listen(sound_source)  #to read the voice of sound_source
            command = listener.recognize_google(voice)  #voice to text
            if 'Sofia' in command:
                command = command.replace('Sofia','')
                print(command)


    except:
        pass
    return command

def run_sofia():
    command = input_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(time)
    elif 'play' in command:
        video = command.replace('play','')
        talk('playing' + video)
        pywhatkit.playonyt(video)
    elif 'about' in command:
        result= command.replace('tell me about', '')
        information = wikipedia.summary(result,2)
        talk(information)
        print(information)
    elif 'search' in command:
        topic = command.replace('search', '')
        talk('searching' + topic)
        pywhatkit.search(topic)
    elif 'what is your name' or 'who are you' in command:
        talk('my name is Sofia.')
    else:
        talk('I am searching it on google for you')
        pywhatkit.search(command)
while True:
    run_sofia()

