def detect_spiral(df, window=5, threshold=-0.2):
    if len(df) < window:
        return False

    recent = df.tail(window)

    negative_count = sum(recent["sentiment"] < threshold)

    return negative_count >= (window - 1)