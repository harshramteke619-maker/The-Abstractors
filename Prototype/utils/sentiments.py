from models.emotion_model import get_emotion_scores, get_sentiment_score
from utils.sentiment import basic_sentiment

def hybrid_sentiment(text):
    transformer_scores = get_emotion_scores(text)
    transformer_sentiment = get_sentiment_score(transformer_scores)

    basic = basic_sentiment(text)

    # Weighted average
    return (0.7 * transformer_sentiment) + (0.3 * basic)