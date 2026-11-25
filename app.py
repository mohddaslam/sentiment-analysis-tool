import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("IMDB.csv")

df = df[["description", "rating"]]

def convert_sentiment(rating):
    if rating >= 7:
        return "positive"
    else:
        return "negative"

df["sentiment"] = df["rating"].apply(convert_sentiment)

df.rename(columns={"description": "review"}, inplace=True)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["review"])

model = LogisticRegression()
model.fit(X, df["sentiment"])

st.set_page_config(page_title="Sentiment Analysis Tool")

st.title("Sentiment Analysis Tool")
st.write("Enter text to analyze sentiment")

user_input = st.text_area("Input Text")
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]

        # Output (ONLY 2 results)
        if prediction == "positive":
            st.success("Positive")
        else:
            st.error("Negative")