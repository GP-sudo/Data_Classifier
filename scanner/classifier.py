# Map detected entities to sensitivity levels
classification_map = {
    "SSN": "Restricted",
    "Credit Card": "Restricted",
    "Email": "Sensitive",
    "Phone": "Sensitive",
    "PERSON": "Sensitive",
    "ORG": "Internal",
    "GPE": "Internal"
}

def classify(findings):
    classified = []
    for f in findings:
        if isinstance(f, tuple):  # from NLP (text, label)
            label = f[1]
        else:  # from regex (string label)
            label = f
        sensitivity = classification_map.get(label, "Public")
        classified.append((f, sensitivity))
    return classified