from transformers import pipeline

fake_news_classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-fake-news-detection"
)

def detect_fake_news(text: str):
    try:
        res = fake_news_classifier(text, truncation=True)[0]

        # Normalisation des labels
        label_map = {
            "LABEL_0": "Fake",
            "LABEL_1": "Real",
            "REAL": "Real",
            "FAKE": "Fake"
        }

        raw_label = res.get("label", "")
        clean_label = label_map.get(raw_label, "UNKNOWN")

        confidence = res.get("score", 0.0)
        confidence_pct = round(confidence * 100, 2)

        # Probabilité de vérité (0-100)
        if clean_label == "Real":
            truth_probability = round(confidence * 100, 2)
            fake_risk = round((1 - confidence) * 100, 2)
        elif clean_label == "Fake":
            truth_probability = round((1 - confidence) * 100, 2)
            fake_risk = round(confidence * 100, 2)
        else:
            truth_probability = 50.0
            fake_risk = 50.0

        # Interprétation humaine
        if truth_probability >= 85:
            verdict = "Très probablement vrai"
        elif truth_probability >= 65:
            verdict = "Plutôt vrai"
        elif truth_probability >= 45:
            verdict = "Incertain"
        elif truth_probability >= 25:
            verdict = "Plutôt faux"
        else:
            verdict = "Très probablement faux"

        # Niveau de confiance
        if confidence_pct >= 90:
            confidence_level = "Élevée"
        elif confidence_pct >= 70:
            confidence_level = "Moyenne"
        else:
            confidence_level = "Faible"

        return {
            "label": clean_label,
            "confidence_pct": confidence_pct,
            "truth_probability": truth_probability,
            "fake_risk": fake_risk,
            "verdict": verdict,
            "confidence_level": confidence_level
        }

    except Exception as e:
        return {
            "label": "ERROR",
            "confidence_pct": 0.0,
            "truth_probability": 50.0,
            "fake_risk": 50.0,
            "verdict": "Indéterminé",
            "confidence_level": "Faible",
            "error": str(e)
        }
