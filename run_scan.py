from scanner.regex_rules import regex_scan
from scanner.nlp_scanner import nlp_scan
from scanner.classifier import classify
from scanner.reporter import generate_report

# Read sample.txt
with open("data/sample.txt", "r") as f:
    text = f.read()

# Run scanners
regex_findings = regex_scan(text)
nlp_findings = nlp_scan(text)
all_findings = regex_findings + nlp_findings

# Classify
classified = classify(all_findings)

# Generate report
report_df = generate_report("sample.txt", classified)
print(report_df)