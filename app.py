import streamlit as st
import pandas as pd
from textblob import TextBlob
from datetime import datetime
import os
import matplotlib.pyplot as plt

FILE = "journal.csv"

# Initialize
if not os.path.exists(FILE):
    pd.DataFrame(columns=["date", "entry", "sentiment"]).to_csv(FILE, index=False)

# Sentiment
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Save entry
def save_entry(entry, sentiment):
    df = pd.read_csv(FILE)
    new = pd.DataFrame([{
        "date": datetime.now(),
        "entry": entry,
        "sentiment": sentiment
    }])
    df = pd.concat([df, new], ignore_index=True)
    df.to_csv(FILE, index=False)

# Detect spiral
def detect_spiral(df):
    if len(df) < 5:
        return False
    last = df.tail(5)
    negative = sum(last["sentiment"] < -0.2)
    return negative >= 4

# UI
st.title("🧠 AI Journaling Companion")
st.write("Your private emotional wellness tracker")

entry = st.text_area("Write your thoughts...")

if st.button("Submit"):
    if entry:
        sentiment = get_sentiment(entry)
        save_entry(entry, sentiment)

        st.success(f"Sentiment Score: {sentiment:.2f}")

        df = pd.read_csv(FILE)

        if detect_spiral(df):
            st.warning("⚠️ You've been feeling low consistently.")
            st.write("Would you like help?")
            st.button("📞 Contact Counsellor")
            st.button("💬 Anonymous Helpline")

# Show trend
if st.button("Show Emotional Trend"):
    df = pd.read_csv(FILE)

    if len(df) > 0:
        plt.plot(df["sentiment"])
        plt.title("Emotional Trend")
        st.pyplot(plt)
    else:
        st.write("No data yet.")