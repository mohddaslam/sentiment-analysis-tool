
# Sentiment Analysis Tool

A machine-learning-based web application that analyzes text and predicts whether the sentiment is Positive or Negative.

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

## Features

- Enter text for sentiment analysis.
- Convert text into numerical features using TF-IDF.
- Predict sentiment using Logistic Regression.
- Display Positive or Negative results.
- Interactive web interface using Streamlit.

## Dataset

The application uses an IMDb movie review dataset containing review descriptions and ratings.

Ratings of 7 or above are classified as Positive. Ratings below 7 are classified as Negative.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd sentiment-analysis-tool
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## Project Purpose

This project was developed to gain practical experience with Python, Natural Language Processing concepts, machine learning, and interactive web application development.
