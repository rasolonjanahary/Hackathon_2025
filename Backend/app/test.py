

from app.extractor import extract_facts

from app.bias import analyze_bias
from app.fake_news import detect_fake_news
from app.services.source_verifier import evaluate_source
from app.services.trust_score import compute_trust_score
texte_test = "Le réchauffement climatique est une réalité scientifique confirmée par 97% des climatologues."
url_test = "https://www.lemonde.fr"

print("🧪 Test du système complet...\n")

# 1. Extraction des faits
faits = extract_facts(texte_test)
print(f"1. Faits extraits : {faits[:2]}")

# 2. Analyse de biais
biais = analyze_bias(texte_test)
print(f"2. Biais détecté : {biais}")

# 3. Détection de fake news
fake = detect_fake_news(texte_test)
print(f"3. Fake news : {fake}")

# 4. Vérification de la source
source_score, details = evaluate_source(url_test)
print(f"4. Score source : {source_score}/100")
print(f"   Détails : {details}")


# 5. Score final
final_score, conclusion = compute_trust_score(
    source_score, 
    biais["bias_score"], 
    fake["label"],
    fake["fake_risk"],
    fake["truth_probability"]
)
print(f"5. SCORE FINAL : {final_score}/100")
print(f"   CONCLUSION : {conclusion}")