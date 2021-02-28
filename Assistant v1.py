import speech_recognition as sr, time as t, webbrowser as wb, sys as s, playsound as ps, os, random, pywhatkit as pwk
from gtts import gTTS
from datetime import datetime as Dt
r = sr.Recognizer()



def recordAudio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Unknown")
        except sr.UnknownValueError:
            speak("speech recognition failed")
        return voice_data

def CheckCommand(voice_data):
    if 'terminate' in voice_data:
        x = speak('terminating')
        exit()

    elif 'update' in voice_data:
        os.execl(s.executable, os.path.abspath(__file__), *s.argv) 
    
    elif "vigo" in voice_data:
        speak("yes?")
    
    elif 'your name' in voice_data:
        speak("my name is Vigo")

    elif 'time' in voice_data:
        now = Dt.now()
        s1 = now.strftime("%m/%d/%Y, %H:%M")
        speak("it's the " + s1)


    elif 'search' in voice_data:
        search = recordAudio('what do you want to search?')
        url = 'https://www.google.com/search?q=' + search
        wb.get().open(url)
        speak('here is what I found for ' + search)
    
    elif 'find location' in voice_data:
        location = recordAudio('where?')
        url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
        wb.get().open(url)
        speak('here is the location of ' + location)

    elif 'play' in voice_data:
        start = voice_data.index('play') + 5
        command = voice_data[start:]
        if 'you know what' in command:
            pwk.playonyt("never gonna give you up")
        else:
            pwk.playonyt(command)

def speak(audio_str, slow = False):
    tts = gTTS(text=audio_str, lang = 'en-uk', slow = slow)
    n = random.randint(0, 100000000)
    audio_file = 'audio-' + str(n) + '.mp3'
    tts.save(audio_file)
    ps.playsound(audio_file) 
    print(audio_str)
    os.remove(audio_file)

def onStart():
    t.sleep(1)
    speak("how can I help you?")
    while 1:
        voice_data = recordAudio()
        print(voice_data)
        CheckCommand(voice_data)

onStart()