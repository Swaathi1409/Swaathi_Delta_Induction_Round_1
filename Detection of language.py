from googletrans import Translator, LANGUAGES

def detect_language(sentence):
    try:
        translator = Translator()
        detected_lang = translator.detect(sentence)
        lang_code = detected_lang.lang
        language = LANGUAGES[lang_code]
        return language
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_sentence = input("Enter a sentence to detect its language: ")
    detected_language = detect_language(input_sentence)
    print(f"Detected language: {detected_language}")
