from fastapi import APIRouter
from .extractor import extract_facts
from .bias import analyze_bias
from .fake_news import detect_fake_news
from .services.source_verifier import evaluate_source
from .services.cross_checker import cross_check_fact
from .services.trust_score import compute_trust_score

router = APIRouter()

@router.post("/analyze")
def analyze(content: str, source_url: str | None = None):
    facts = extract_facts(content)
    bias = analyze_bias(content)
    fake = detect_fake_news(content)

    source_score, source_details = evaluate_source(source_url)

    cross_results = []
    for fact in facts:
        cross_results.append({
            "fact": fact,
            "results": cross_check_fact(fact)
        })

    final_score, conclusion = compute_trust_score(
        source_score,
        bias["bias_score"],
        fake["label"],
        fake["fake_risk"],
        fake["truth_probability"]
    )

    return {
        "input": content,
        "scores": {
            "source": source_score,
            "bias": bias,
            "fake_news": fake,
            "final": final_score
        },
        "source_details": source_details,
        "cross_checking": cross_results,
        "conclusion": conclusion
    }
