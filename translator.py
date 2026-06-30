from deep_translator import GoogleTranslator

def translate_to_english(text, language):
    if language == "en":
        return text

    try:
        return GoogleTranslator(source=language, target="en").translate(text)
    except:
        return text


def translate_from_english(text, language):
    if language == "en":
        return text

    try:
        return GoogleTranslator(source="en", target=language).translate(text)
    except:
        return text