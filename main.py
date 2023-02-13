import time
import speech_recognition
import speech_recognition as sr
import pyttsx3
from chatgpt import sample_response

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
try:
    def talk(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'jarvis' in command:
                    command = command.replace('jarvis', '')
                    print(command)
        except UnboundLocalError:
            pass
        except speech_recognition.UnknownValueError:
            pass
        return command
    def run_alex():
        try:
            command = take_command()
            s =sample_response(command)
            print(s)
            talk(s)

        except UnboundLocalError:
            pass


    while True:
        time.sleep(1)
        run_alex()
except KeyError:
    pass
except KeyboardInterrupt:
    pass
