import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def translate_audio():
    recognizer = sr.Recognizer()
    translator = Translator()
    engine = pyttsx3.init()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        translated_text = translator.translate(text, dest='af').text
        print("Translation:", translated_text)
        
        # Speak the translated text
        engine.say(translated_text)
        engine.runAndWait()
        
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        translate_audio()
