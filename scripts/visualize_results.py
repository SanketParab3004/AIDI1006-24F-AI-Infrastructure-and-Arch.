import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_pie_chart(df, column, title, output_filename, max_categories=10):
    # Get sentiment counts
    sentiment_counts = df[column].value_counts()

    # If there are more than 'max_categories', group the smaller categories into 'Other'
    if len(sentiment_counts) > max_categories:
        # Group the smaller categories into 'Other'
        sentiment_counts = sentiment_counts.head(max_categories)
        other_count = sentiment_counts.tail(-max_categories).sum()
        if other_count > 0:
            sentiment_counts = sentiment_counts.append(pd.Series({'Other': other_count}))

    # Plot the pie chart
    sentiment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.ylabel('')  # Hide y-axis label
    plt.savefig(f"outputs/{output_filename}")
    plt.show()


def plot_wordcloud(df, text_column, output_filename):
    # Join all text into one large string
    text = " ".join(df[text_column].dropna())  # Drop NaN values just in case
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(f"outputs/{output_filename}")
    plt.show()

def visualize_results():
    # Load sentiment analysis results
    df = pd.read_csv("data/results/sentiment_analysis_results.csv")

    # Check for the existence of 'textblob_sentiment'
    if 'textblob_sentiment' not in df.columns:
        print("TextBlob sentiment column not found. Adding sentiment analysis...")
        from textblob import TextBlob

        # Define a function to calculate TextBlob sentiment
        def textblob_sentiment(text):
            if isinstance(text, str):
                return TextBlob(text).sentiment.polarity
            else:
                return 0.0

        # Apply TextBlob sentiment analysis to the 'cleaned_text' column
        df['textblob_sentiment'] = df['cleaned_text'].apply(textblob_sentiment)

        # Save the updated dataframe with the new sentiment column
        df.to_csv("data/results/sentiment_analysis_results.csv", index=False)

    # Plot pie charts for sentiment distributions
    plot_pie_chart(df, 'vader_sentiment', "VADER Sentiment Distribution", "vader_sentiment_pie.png")
    plot_pie_chart(df, 'textblob_sentiment', "TextBlob Sentiment Distribution", "textblob_sentiment_pie.png")

    # Plot Wordcloud
    plot_wordcloud(df, 'cleaned_text', "wordcloud.png")
