try:
    from googletrans import Translator
except ImportError:
    Translator = None

# Dictionary-based fallback translation
TRANSLATION_MAP = {
    "hello": "ಹಲೋ",
    "goodbye": "ಗೋಡ್‌ಬೈ",
    "thank you": "ಧನ್ಯವಾದಗಳು",
    "yes": "ಹೌದು",
    "no": "ಇಲ್ಲ",
    "good morning": "ಶುಭೋದಯ",
    "good night": "ಶುಭರಾತ್ರಿ",
    "how are you": "ನೀವು ಹೇಗಿದ್ದೀರಿ",
    "what is your name": "ನಿಮ್ಮ ಹೆಸರು ಏನು",
    "please": "ದಯವಿಟ್ಟು",
    "excuse me": "ನನ್ನನ್ನು ಕ್ಷಮಿಸಿ",
    "i love you": "ನಾನು ನಿಮ್ಮನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ",
    "help": "ಸಹಾಯ",
    "water": "ನೀರು",
    "food": "ಆಹಾರ"
}

def translate(text):
    """Translate English text to Kannada"""
    if not text:
        return ""
    
    text_lower = text.lower().strip()
    
    # Check if exact match exists in dictionary
    if text_lower in TRANSLATION_MAP:
        return TRANSLATION_MAP[text_lower]
    
    # Try online translation if available
    if Translator:
        try:
            translator = Translator()
            translation = translator.translate(text, src='en', dest='kn')
            return translation['text']
        except Exception as e:
            print(f"Online translation failed: {e}")
            # Fall back to dictionary translation for first word
            first_word = text_lower.split()[0] if text_lower else text
            return TRANSLATION_MAP.get(first_word, text)
    
    # Fall back to dictionary translation
    first_word = text_lower.split()[0] if text_lower else text
    return TRANSLATION_MAP.get(first_word, f"[Translation not available for: {text}]")

# Alias for compatibility with app.py
def translate_text(text):
    return translate(text)

def main():
    # Example usage
    english_text = "Hello, how are you?"
    kannada_translation = translate_text(english_text)
    print(f"English: {english_text}")
    print(f"Kannada: {kannada_translation}")

if __name__ == "__main__":
    main()