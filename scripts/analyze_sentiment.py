import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(text):
    if isinstance(text, str):  # Ensure the text is a string
        return vader_analyzer.polarity_scores(text)['compound']
    else:
        return 0.0  # Return neutral sentiment for non-string inputs

def textblob_sentiment(text):
    if isinstance(text, str):
        # Get polarity using TextBlob
        blob = TextBlob(text)
        return blob.sentiment.polarity
    else:
        return 0.0  # Return neutral sentiment for non-string inputs

def analyze_sentiment():
    # Load cleaned data
    df = pd.read_csv("data/cleaned/cleaned_clean_d_tweets.csv")
    
    # Apply VADER sentiment analysis
    df['vader_sentiment'] = df['cleaned_text'].apply(vader_sentiment)
    
    # Apply TextBlob sentiment analysis
    df['textblob_sentiment'] = df['cleaned_text'].apply(textblob_sentiment)
    
    # Save the results with both VADER and TextBlob sentiments
    df.to_csv("data/results/textblob_vader_sentiment_results.csv", index=False)
    print("Sentiment analysis (VADER & TextBlob) saved to data/results/textblob_vader_sentiment_results.csv")

    # Optionally, you can also return the DataFrame for further analysis
    return df

if __name__ == "__main__":
    analyze_sentiment()
