import pandas as pd
import os
from datetime import datetime

DATA_FILE = "data/journal.csv"

def init_storage():
    # Create folder if not exists
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "entry", "sentiment"])
        df.to_csv(DATA_FILE, index=False)


def load_data():
    return pd.read_csv(DATA_FILE)


def save_entry(entry, sentiment):
    df = load_data()

    new_row = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entry": entry,
        "sentiment": sentiment
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)