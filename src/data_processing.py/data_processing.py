import pandas as pd
import re
from wordcloud import STOPWORDS

# Check for missing values
missing_values = news_df.isnull().sum()

# Add a column for news length (number of words)
news_df['news_length'] = news_df['news'].apply(lambda x: len(x.split()))

# Define stop words and regex pattern to clean text
stop_words = set(STOPWORDS)
pattern = r'\b\w{1,2}\b|\d+'  # Remove short words (1-2 chars) and numbers

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(pattern, '', text)
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

# Apply cleaning function
news_df['cleaned_news'] = news_df['news'].apply(clean_text)

# Save processed dataset
news_df.to_csv('processed_news.csv', index=False)