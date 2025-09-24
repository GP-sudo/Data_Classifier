import spacy

# Load pre-trained English model
nlp = spacy.load("en_core_web_sm")

def nlp_scan(text):
    """
    Scans text for named entities (PERSON, ORG, GPE, LOC)
    Returns a list of tuples: (entity_text, entity_label)
    """
    doc = nlp(text)
    findings = []
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]:
            findings.append((ent.text, ent.label_))
    return findings

text = "Alice Johnson works at Google in California."
print(nlp_scan(text))
# Output: [('Alice Johnson', 'PERSON'), ('Google', 'ORG'), ('California', 'GPE')]

"""
To test run the file code
❯ source venv/bin/activate
❯ python
from scanner.nlp_scanner import nlp_scan
"""