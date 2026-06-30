import pandas as pd
from language import detect_language
from translator import translate_to_english, translate_from_english
from sentiment import predict_sentiment
from responses import get_bot_response

# Load dataset
data = pd.read_csv("data/sample_data.csv")

# Search dataset
def search_dataset(question):
    question = question.lower().strip()

    for _, row in data.iterrows():
        if question == str(row["question"]).lower().strip():
            return row["answer"]

    return None

def get_response(user_input):

    # Detect language
    language = detect_language(user_input)

    # Translate input to English
    english_text = translate_to_english(user_input, language)

    # Predict sentiment
    sentiment = predict_sentiment(english_text)

    # Search in dataset
    dataset_answer = search_dataset(english_text)

    if dataset_answer:
        response = dataset_answer
    else:
        # Use predefined chatbot responses
        response = get_bot_response(english_text, sentiment, language)

    # Translate response back to user's language
    final_response = translate_from_english(response, language)

    return final_response