def predict_sentiment(text):
    text = text.lower()

    positive_words = [
        "good", "great", "happy", "excellent",
        "awesome", "love", "nice", "thank you"
    ]

    negative_words = [
        "bad", "sad", "angry", "hate",
        "terrible", "worst", "poor", "problem"
    ]

    for word in positive_words:
        if word in text:
            return "Positive"

    for word in negative_words:
        if word in text:
            return "Negative"

    return "Neutral"