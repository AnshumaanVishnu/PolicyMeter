# Functions for analyzing the sentiment of text data

def analyze_sentiment(text):
    """
    Placeholder function for sentiment analysis.
    A real implementation would use a library like NLTK, spaCy, or a pre-trained model.
    """
    print(f"Analyzing sentiment for: '{text}'")
    # Dummy logic: if 'praise' or 'great' is in the text, it's positive.
    # If 'concerns' or 'rushed' is in the text, it's negative.
    if "praise" in text.lower() or "great" in text.lower():
        return "Positive"
    elif "concerns" in text.lower() or "rushed" in text.lower():
        return "Negative"
    else:
        return "Neutral"

def analyze_dataset(data):
    """
    Analyzes the sentiment of a dataset of text entries.
    """
    results = []
    for item in data:
        text_to_analyze = item.get("headline") or item.get("text")
        if text_to_analyze:
            sentiment = analyze_sentiment(text_to_analyze)
            results.append({"text": text_to_analyze, "sentiment": sentiment})
    return results
