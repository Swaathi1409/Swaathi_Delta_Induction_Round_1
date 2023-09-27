from googletrans import Translator

def translate_to_english(sentence, target_language='en'):
    try:
        translator = Translator()
        translated = translator.translate(sentence, dest=target_language)
        return translated.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    input_sentence = input("Enter your sentence:")
    translated_sentence = translate_to_english(input_sentence)
    print(f"This sentence translates to: {translated_sentence}")

