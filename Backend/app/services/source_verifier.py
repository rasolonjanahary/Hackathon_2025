def evaluate_source(url: str | None):
    score = 50
    details = {
        "authority": False,
        "traceability": False,
        "reputation": False,
        "transparency": False
    }

    if not url:
        return score, details

    if any(tld in url for tld in [".gov", ".edu", ".int"]):
        score += 20
        details["authority"] = True

    if "about" in url or "contact" in url:
        score += 10
        details["transparency"] = True

    if "wikipedia" in url or "who.int" in url:
        score += 20
        details["reputation"] = True

    details["traceability"] = True
    return min(score, 100), details
