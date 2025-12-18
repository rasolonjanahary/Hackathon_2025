from transformers import pipelines

fake_news_classifier = pipelines(
    "text-classification",
    model="jy46604790/Fake-News-Bert-Classification"
)

def detect_fake_news(text: str):
    res = fake_news_classifier(text)[0]

    return {
        "label": res["label"],   # FAKE / REAL
        "confidence": round(res["score"] * 100, 2)
    }
