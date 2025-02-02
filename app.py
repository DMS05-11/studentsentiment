import streamlit as st
import pandas as pd
from textblob import TextBlob

# Function to analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Streamlit App UI
st.title("📊 Student Feedback Sentiment Analysis")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Show uploaded data
    st.subheader("Uploaded Data Preview")
    st.write(df.head())

    # Process Sentiment Analysis
    df["Sentiment"] = df["Feedback Text"].apply(get_sentiment)
    
    # Show sentiment results
    st.subheader("Sentiment Analysis Results")
    st.write(df)

    # Count plot
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["Sentiment"].value_counts())

    # Download processed data
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(label="Download Analyzed Data", data=csv, file_name="sentiment_results.csv", mime="text/csv")
