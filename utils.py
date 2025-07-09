from langdetect import detect, DetectorFactory
from googletrans import Translator

DetectorFactory.seed = 0
translator = Translator()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Unknown"

def translate_text(text, dest_lang):
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"
