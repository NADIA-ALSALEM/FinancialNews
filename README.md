# Financial News Classification with Streamlit

## Overview

This project involves creating a **Financial News Classification** application using **Streamlit** and **Python**. The application allows users to input financial news text, and it classifies the sentiment of the news as either **Positive** or **Negative** using a pre-trained **Logistic Regression** model and a **TF-IDF vectorizer**.

---

## Key Features

### User-Friendly Interface:
- Built using **Streamlit**, the app provides a clean and interactive interface for users to input financial news text.
- Includes a text area for input and a button to trigger the classification process.

### Sentiment Classification:
- The app uses a pre-trained **Logistic Regression** model to predict the sentiment of the input text.
- The input text is first transformed into a **TF-IDF** vector for model compatibility.

### Visual Enhancements:
- The app includes visual feedback for predictions:
  - **Positive sentiment**: Displays a success message with a celebratory balloon effect.
  - **Negative sentiment**: Displays an error message with a snow effect.
- A **placeholder image** is added at the top of the page to make the interface more engaging.

---

## Technical Details

- **Model**: A pre-trained **Logistic Regression** model is used for sentiment classification.
- **Vectorizer**: The **TF-IDF** vectorizer is used to convert text into numerical features for the model.
- **Streamlit**: The app is built using **Streamlit**, a powerful framework for creating web apps with Python.

---

## How It Works

1. The user inputs **financial news text** into the provided text area.
2. The app preprocesses the text using the **TF-IDF vectorizer**.
3. The **Logistic Regression** model predicts the sentiment (**Positive** or **Negative**).
4. The result is displayed with a visual effect:
   - **Balloons** for positive sentiment.
   - **Snow** for negative sentiment.

---

## Installation

To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/financial-news-classification.git
   cd financial-news-classification
