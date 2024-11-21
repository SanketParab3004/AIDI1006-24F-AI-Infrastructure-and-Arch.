# Sentiment Analysis on Tweets

## AIDI1006-24F-AI-Infrastructure-and-Arch.

This repository contains a sentiment analysis solution built using Python. It uses **VADER** and **TextBlob** libraries to analyze the sentiment of tweets and visualize the results using various charts and word clouds.

## Project Overview

This project processes a collection of tweets, performs sentiment analysis using two popular libraries, and then generates visualizations including pie charts and word clouds. The primary goal is to understand the sentiment behind tweets and present it in an interactive and visually appealing way.

## Features

- **Sentiment Analysis** using VADER and TextBlob
- **Visualization** of sentiment distribution with pie charts
- **Word Cloud** to visualize the most common words in tweets
- **Interactive Dashboard** (optional)
  
## Technologies Used

- Python
- Libraries:
  - **Pandas** for data handling
  - **Matplotlib** for visualization
  - **WordCloud** for generating word clouds
  - **TextBlob** for sentiment analysis
  - **VADER** for sentiment analysis

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pip (for installing dependencies)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. Create and activate a virtual environment (optional, but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Step 1: Load Data

Ensure you have the dataset ready in the `data/` directory. The dataset should contain a column for the tweets (`'cleaned_text'` column), which will be used for sentiment analysis.

### Step 2: Perform Sentiment Analysis

Run the `sentiment_analysis.py` script to perform sentiment analysis on the tweets:

```bash
python sentiment_analysis.py
```

This will process the data and create a CSV file (`sentiment_analysis_results.csv`) with sentiment scores for each tweet.

### Step 3: Visualize Results

To generate visualizations (pie charts and word clouds), run the `visualize_results.py` script:

```bash
python visualize_results.py
```

This will output:

- A pie chart showing the sentiment distribution of the tweets (`vader_sentiment_pie.png` and `textblob_sentiment_pie.png`)
- A word cloud (`wordcloud.png`) representing the most common words in the tweets.

### Optional: Interactive Dashboard

For a more interactive experience, you can integrate your visualizations into a dashboard using a framework like Dash or Flask. For now, this setup is focused on generating static visualizations.

## Project Structure

```
sentiment-analysis/
├── data/
│   └── sentiment_analysis_results.csv        # The output of sentiment analysis
├── outputs/
│   ├── vader_sentiment_pie.png              # VADER sentiment pie chart
│   ├── textblob_sentiment_pie.png           # TextBlob sentiment pie chart
│   └── wordcloud.png                        # Word cloud image
├── requirements.txt                        # Python dependencies
├── sentiment_analysis.py                   # Script to perform sentiment analysis
└── visualize_results.py                    # Script to generate visualizations
```

## Contributing

Feel free to fork this project, submit issues, or contribute improvements. If you would like to contribute, make sure to follow the standard GitHub fork and pull request workflow.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Example of **requirements.txt**

```
pandas
matplotlib
wordcloud
textblob
vaderSentiment
```

---

This **README.md** file includes setup instructions, running the analysis, and generating results. You can expand or modify it depending on additional functionality you implement in your project.
