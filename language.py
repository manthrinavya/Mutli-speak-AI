from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def detect_language(text):
    text = text.lower()

    # Hindi script
    if any('\u0900' <= ch <= '\u097F' for ch in text):
        return "hi"

    # Telugu script
    if any('\u0C00' <= ch <= '\u0C7F' for ch in text):
        return "te"

    # Roman Hindi words
    roman_hindi = [
        "aap", "kaun", "ho", "mera", "naam", "mujhe",
        "main", "mai", "hai", "kya", "kaise",
        "namaste", "dhanyavaad", "shukriya"
    ]

    # Roman Telugu words
    roman_telugu = [
        "meeru", "evaru", "ela", "unnaru", "nenu",
        "na", "peru", "enti", "namaskaram",
        "bagunnara", "avunu", "kaadu"
    ]

    words = text.split()

    if any(word in words for word in roman_hindi):
        return "hi"

    if any(word in words for word in roman_telugu):
        return "te"

    try:
        lang = detect(text)

        if lang in ["en", "de"]:
            return lang
        elif lang in ["hi", "te"]:
            return lang
        else:
            return "en"

    except:
        return "en"
