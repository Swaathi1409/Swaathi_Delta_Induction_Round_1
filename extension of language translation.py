from googletrans import Translator
lang = input("Enter the language code of preferred language:")

def translate_to_random_lang(sentence, target_language=  lang):
    try:
        translator = Translator()
        translated = translator.translate(sentence, dest=target_language)
        return translated.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_sentence = input("Enter your sentence:")
    translated_sentence = translate_to_random_lang(input_sentence)
    print(f"Translated to:{translated_sentence}")
