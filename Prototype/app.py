import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from models.emotion_model import get_emotion_scores, get_sentiment_score
from utils.storage import init_storage, load_data, save_entry
from utils.spiral_detection import detect_spiral

# ---------------------
# INIT
# ---------------------
st.set_page_config(page_title="AI Journal Companion", layout="centered")
init_storage()

st.title("🧠 AI Journaling Companion")
st.write("Write freely. No judgment. Just you.")

# ---------------------
# INPUT
# ---------------------
entry = st.text_area("How are you feeling today?")

if st.button("Submit"):
    if entry.strip() == "":
        st.warning("Please write something.")
    else:
        with st.spinner("Analyzing emotions..."):
            scores = get_emotion_scores(entry)
            sentiment = get_sentiment_score(scores)

        save_entry(entry, sentiment)

        # Feedback
        if sentiment > 0:
            st.success("😊 You seem to be feeling positive!")
        elif sentiment < 0:
            st.info("💙 It's okay to feel low sometimes.")
        else:
            st.info("😐 Neutral mood detected.")

# ---------------------
# LOAD DATA
# ---------------------
df = load_data()

if len(df) > 0:
    df["date"] = pd.to_datetime(df["date"])

    st.subheader("📊 Emotional Trend")

    fig, ax = plt.subplots()
    ax.plot(df["date"], df["sentiment"], marker='o')
    ax.axhline(0, linestyle='--')
    ax.set_ylabel("Sentiment Score")
    ax.set_xlabel("Time")

    st.pyplot(fig)

# ---------------------
# SPIRAL DETECTION
# ---------------------
if len(df) > 0 and detect_spiral(df):
    st.warning("⚠️ You've been feeling low consistently.")

    st.write("You're not alone. Talking might help 💙")

    if st.button("Show Support Options"):
        st.markdown("""
        ### 🤝 Support Options (Opt-in)

        - Campus Counselor
        - Trusted Friend / Family
        - Online Therapy Platforms
        - India Helpline: **9152987821**

        Take your time. You're in control.
        """)

# ---------------------
# PRIVACY
# ---------------------
st.caption("🔒 Data is stored locally. No tracking.")