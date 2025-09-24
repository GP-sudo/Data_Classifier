import re

# Common regex patterns for PII
patterns = {
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "Credit Card": r"\b(?:\d[ -]*?){13,16}\b",
    "Email": r"[a-zA-Z0-9+._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone": r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b"
}

def regex_scan(text):      #text can be any string (e.g., a row, a column value, or the whole file content).
    findings = []           # empty list
    for label, pattern in patterns.items(): #label → the name of the type of sensitive data (e.g., "SSN").
        if re.search(pattern, text): # Returns true if pattern found in text
            findings.append(label)
    return findings


if __name__ == "__main__":
    test_text = "Alice Johnson alice.johnson@example.com 123-45-6789 555-123-4567 4111-1111-1111-1111"
    print("Test Findings:", regex_scan(test_text))

"""	 b → word boundary
	\d{3} → area code (3 digits)
	[-.\s]?? → optional separator (dash, dot, or space) — lazy match
	\d{3} → next 3 digits
	\d{4} → last 4 digits
"""