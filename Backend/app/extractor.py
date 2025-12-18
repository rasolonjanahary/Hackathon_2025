import spacy

try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    # Télécharger automatiquement
    print("Modèle 'fr_core_news_sm' non trouvé. Téléchargement en cours...")

def extract_facts(text: str):
    doc = nlp(text)
    facts = []
    for sent in doc.sents:
        if len(sent.text.strip()) > 10:
            facts.append(sent.text.strip())
    return facts
