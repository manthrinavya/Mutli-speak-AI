def get_bot_response(user_input, sentiment, language):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey", "namaste", "namaskaram"]):

        if language == "hi":
            return "Namaste! Main aapki kaise madad kar sakta hoon? (नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?)"

        elif language == "te":
            return "Namaskaram! Nenu meeku ela sahayam cheyagalanu? (నమస్కారం! నేను మీకు ఎలా సహాయం చేయగలను?)"

        elif language == "de":
            return "Hallo! Wie kann ich Ihnen helfen?"

        else:
            return "Hello! How can I help you today?"

    # Who are you
    elif "who are you" in user_input or "kaun ho" in user_input or "evaru" in user_input:

        if language == "hi":
            return "Main ek bahubhashi chatbot hoon. (मैं एक बहुभाषी चैटबॉट हूँ।)"

        elif language == "te":
            return "Nenu bahu bhasha chatbot ni. (నేను బహుభాషా చాట్‌బాట్‌ని.)"

        elif language == "de":
            return "Ich bin ein mehrsprachiger Chatbot."

        else:
            return "I am a multilingual chatbot."

    # AI
    elif "ai" in user_input:

        if language == "hi":
            return "AI ka matlab Artificial Intelligence hai. (एआई का मतलब कृत्रिम बुद्धिमत्ता है।)"

        elif language == "te":
            return "AI ante Artificial Intelligence. (ఏఐ అంటే కృత్రిమ మేధస్సు.)"

        elif language == "de":
            return "KI steht für Künstliche Intelligenz."

        else:
            return "AI stands for Artificial Intelligence."

    # Python
    elif "python" in user_input:

        if language == "hi":
            return "Python ek popular programming language hai. (पायथन एक लोकप्रिय प्रोग्रामिंग भाषा है।)"

        elif language == "te":
            return "Python oka popular programming language. (పైథాన్ ఒక ప్రముఖ ప్రోగ్రామింగ్ భాష.)"

        elif language == "de":
            return "Python ist eine beliebte Programmiersprache."

        else:
            return "Python is a popular programming language."

    # Sentiment responses
    elif sentiment == "Positive":

        if language == "hi":
            return "Mujhe khushi hui! 😊 (मुझे खुशी हुई!)"

        elif language == "te":
            return "Naaku santoshamga undi! 😊 (నాకు సంతోషంగా ఉంది!)"

        elif language == "de":
            return "Das freut mich! 😊"

        else:
            return "I'm glad to hear that! 😊"

    elif sentiment == "Negative":

        if language == "hi":
            return "Mujhe afsos hai. Main madad karunga. 😊 (मुझे अफसोस है। मैं मदद करूँगा।)"

        elif language == "te":
            return "Baadhapadakandi. Nenu sahayam chestanu. 😊 (బాధపడకండి. నేను సహాయం చేస్తాను.)"

        elif language == "de":
            return "Es tut mir leid. Ich helfe Ihnen. 😊"

        else:
            return "I'm sorry to hear that. How can I help? 😊"

    else:

        if language == "hi":
            return "Kripya aur jaankari dijiye. (कृपया और जानकारी दीजिए।)"

        elif language == "te":
            return "Dayachesi inka vivaranga cheppandi. (దయచేసి ఇంకా వివరంగా చెప్పండి.)"

        elif language == "de":
            return "Können Sie bitte mehr Informationen geben?"

        else:
            return "That's interesting! Could you tell me more?"