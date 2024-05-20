import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Translator")
        
        self.selected_language = tk.StringVar()
        self.languages = self.get_languages()

        self.create_widgets()
        
    def get_languages(self):
        # Language codes and names
        languages = {
            "af": "African",
            "am": "Amharic",
            "ar": "Arabic",
            "eu": "Basque",
        "bn": "Bengali",
        "en-GB": "English (UK)",
        "pt-BR": "Portuguese (Brazil)",
        "bg": "Bulgarian",
        "ca": "Catalan",
        "chr": "Cherokee",
        "hr": "Croatian",
        "cs": "Czech",
        "da": "Danish",
        "nl": "Dutch",
        "en": "English (US)",
        "et": "Estonian",
        "fil": "Filipino",
        "fi": "Finnish",
        "fr": "French",
        "de": "German",
        "el": "Greek",
        "gu": "Gujarati",
        "iw": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "is": "Icelandic",
        "id": "Indonesian",
        "it": "Italian",
        "ja": "Japanese",
        "kn": "Kannada",
        "ko": "Korean",
        "lv": "Latvian",
        "lt": "Lithuanian",
        "ms": "Malay",
        "ml": "Malayalam",
        "mr": "Marathi",
        "no": "Norwegian",
        "pl": "Polish",
        "pt-PT": "Portuguese (Portugal)",
        "ro": "Romanian",
        "ru": "Russian",
        "sr": "Serbian",
        "zh-CN": "Chinese (PRC)",
        "sk": "Slovak",
        "sl": "Slovenian",
        "es": "Spanish",
        "sw": "Swahili",
        "sv": "Swedish",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "zh-TW": "Chinese (Taiwan)",
        "tr": "Turkish",
        "ur": "Urdu",
        "uk": "Ukrainian",
        "vi": "Vietnamese",
        "cy": "Welsh"
        }
        return languages
        
    def create_widgets(self):
        # Language selection dropdown
        ttk.Label(self.root, text="Select a language to translate to:").grid(row=0, column=0)
        self.language_dropdown = ttk.Combobox(self.root, values=list(self.languages.values()), textvariable=self.selected_language)
        self.language_dropdown.grid(row=0, column=1)
        self.language_dropdown.current(0)
        
        # Start translation button
        self.translate_button = ttk.Button(self.root, text="Start Translation", command=self.translate_audio)
        self.translate_button.grid(row=1, columnspan=2)
        
        # Text display
        self.output_text = tk.Text(self.root, height=10, width=40)
        self.output_text.grid(row=2, columnspan=2)
        
        # Listening label
        self.listening_label = ttk.Label(self.root, text="Not listening")
        self.listening_label.grid(row=3, columnspan=2)
        
    def translate_audio(self):
        selected_language = next(key for key, value in self.languages.items() if value == self.selected_language.get())

        recognizer = sr.Recognizer()
        translator = Translator()
        engine = pyttsx3.init()

        with sr.Microphone() as source:
            self.listening_label.config(text="Listening...")  # Update label text
            self.root.update()  # Update GUI
            audio = recognizer.listen(source)
            self.listening_label.config(text="Not listening")  # Reset label text after listening
            self.root.update()  # Update GUI

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            translated_text = translator.translate(text, dest=selected_language).text
            print("Translation:", translated_text)

            # Display translated text
            self.output_text.insert(tk.END, "Original: " + text + "\n")
            self.output_text.insert(tk.END, "Translation: " + translated_text + "\n")

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
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
