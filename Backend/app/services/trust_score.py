def compute_trust_score(source_score, bias_score, fake_label):
    score = source_score

    if fake_label == "FAKE":
        score -= 30

    if bias_score > 75:
        score -= 20
    elif bias_score > 60:
        score -= 10

    score = max(0, min(score, 100))

    if score >= 80:
        conclusion = "Vrai"
    elif score >= 60:
        conclusion = "Partiellement Vrai"
    else:
        conclusion = "Faux"

    return score, conclusion
