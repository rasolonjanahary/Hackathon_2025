from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_bias(text: str):
    result = sentiment_pipeline(text)[0]
    score = result["score"]

    if score > 0.85:
        level = "Élevé"
    elif score > 0.65:
        level = "Moyen"
    else:
        level = "Faible"

    return {
        "label": result["label"],
        "bias_level": level,
        "bias_score": round(score * 100, 2)
    }
