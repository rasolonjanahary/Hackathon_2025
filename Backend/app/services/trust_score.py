def compute_trust_score(
    source_score: int,
    bias_score: float,
    fake_label: str,
    fake_risk: float,
    truth_probability: float
):
    """
    source_score      : 0-100
    bias_score        : 0-100
    fake_risk         : 0-100
    truth_probability : 0-100
    """

    # Base = vérité estimée
    score = truth_probability * 0.5 + source_score * 0.5

    # Verifiena ilay risque de fake pondéré
    if fake_risk > 80:
        score -= 30
    elif fake_risk > 60:
        score -= 20
    elif fake_risk > 40:
        score -= 10

    # calcule de l'impact du biais sur le score final
    if bias_score > 85:
        score -= 10
    elif bias_score > 70:
        score -= 5

    # verification finale si le fake_label est Real et truth_probability corrrespond bien l'interpretation
    if truth_probability > 90 and fake_label == "Real":
        score = max(score, 70)

    score = max(0, min(round(score, 2), 100))

    # Conclusion basé du score
    if score >= 85:
        conclusion = "Vrai"
    elif score >= 65:
        conclusion = "Plutôt vrai"
    elif score >= 45:
        conclusion = "Incertain"
    else:
        conclusion = "Faux"

    return score, conclusion
