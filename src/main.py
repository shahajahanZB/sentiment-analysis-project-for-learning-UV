from transformers import pipeline

def analyze_sentiment(text: str):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)
    return result

if __name__ == "__main__":
    text = input("Enter text for sentiment analysis: ")
    print(analyze_sentiment(text))
