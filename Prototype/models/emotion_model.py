from transformers import pipeline

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def get_emotion_scores(text):
    results = emotion_pipeline(text)

    # 🔥 Handle nested structure safely
    if isinstance(results, list) and len(results) > 0:
        results = results[0]

    # Ensure it's list of dicts
    if isinstance(results, list):
        scores = {item['label']: item['score'] for item in results}
    else:
        # fallback (rare case)
        scores = {results['label']: results['score']}

    return scores


def get_sentiment_score(scores):
    positive = scores.get("joy", 0)

    negative = (
        scores.get("sadness", 0)
        + scores.get("anger", 0)
        + scores.get("fear", 0)
    )

    return positive - negative