import streamlit as st
import pandas as pd
from scanner.regex_rules import regex_scan
from scanner.nlp_scanner import nlp_scan
from scanner.classifier import classify
from scanner.reporter import generate_report

st.title("🔐 Sensitive Data Discovery & Classification Tool")

uploaded_file = st.file_uploader("Upload a file (CSV/TXT)", type=["csv", "txt"])

if uploaded_file:
    text_data = uploaded_file.read().decode("utf-8")

    # Run scanners
    regex_findings = regex_scan(text_data)
    nlp_findings = nlp_scan(text_data)

    # Combine findings
    findings = regex_findings + nlp_findings

    # Classify sensitivity
    classified = classify(findings)

    # Generate report
    report_df = generate_report(uploaded_file.name, classified)

    st.write("### Findings Report")
    st.dataframe(report_df)