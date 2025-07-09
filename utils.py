from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator

DetectorFactory.seed = 0

def detect_language(text):
    try:
        return detect(text)
    except:
        return "Unknown"

def translate_text(text, dest_lang):
    try:
        return GoogleTranslator(target=dest_lang).translate(text)
    except Exception as e:
        return f"Error: {str(e)}"
