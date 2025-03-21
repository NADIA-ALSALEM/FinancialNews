import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load processed dataset
news_df = pd.read_csv('processed_news.csv')

# Sentiment distribution
sentiment_distribution = news_df['sentiment'].value_counts(normalize=True) * 100

# Function to get most common words
def get_top_words(texts, n=20):
    words = ' '.join(texts).split()
    return Counter(words).most_common(n)

# Get top words for positive and negative news
positive_words = get_top_words(news_df[news_df['sentiment'] == 'POSITIVE']['cleaned_news'])
negative_words = get_top_words(news_df[news_df['sentiment'] == 'NEGATIVE']['cleaned_news'])

# Generate word clouds
def generate_wordcloud(words, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(words))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

generate_wordcloud(positive_words, 'Positive Word Cloud')
generate_wordcloud(negative_words, 'Negative Word Cloud')
