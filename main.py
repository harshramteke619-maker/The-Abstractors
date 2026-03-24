from textblob import TextBlob
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

FILE = "journal_data.csv"

# Initialize file if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["date", "entry", "sentiment"])
    df.to_csv(FILE, index=False)

# Function: Analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # -1 to +1

# Function: Save entry
def save_entry(entry, sentiment):
    df = pd.read_csv(FILE)
    new_row = {
        "date": datetime.now(),
        "entry": entry,
        "sentiment": sentiment
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(FILE, index=False)

# Function: Detect negative spiral
def detect_spiral():
    df = pd.read_csv(FILE)

    if len(df) < 5:
        return False

    last_entries = df.tail(5)

    # Count negative days
    negative_days = sum(last_entries["sentiment"] < -0.2)

    if negative_days >= 4:
        return True

    return False

# Function: Show trend
def show_trend():
    df = pd.read_csv(FILE)
    if len(df) == 0:
        print("No data yet.")
        return

    plt.plot(df["sentiment"])
    plt.title("Emotional Trend Over Time")
    plt.xlabel("Entries")
    plt.ylabel("Sentiment (-1 to +1)")
    plt.show()

# MAIN LOOP
while True:
    print("\n1. Write Journal")
    print("2. Show Emotional Trend")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        entry = input("\nWrite your journal entry:\n")

        sentiment = analyze_sentiment(entry)
        save_entry(entry, sentiment)

        print(f"\nSentiment Score: {sentiment:.2f}")

        # Detect spiral
        if detect_spiral():
            print("\n⚠️ We’ve noticed you’ve been feeling low consistently.")
            print("Would you like to explore support options?")
            print("-> Campus Counsellor")
            print("-> Anonymous Helpline")
            print("-> Mental Health Resources")

    elif choice == "2":
        show_trend()

    elif choice == "3":
        break

    else:
        print("Invalid choice")