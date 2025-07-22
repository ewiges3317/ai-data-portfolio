# FERPA Anonymizer Project Overview

## Problem
Modern AI tools are being used for analytics and automation tasks in education, but administrators fear violating FERPA because large language models (LLMs) can inadvertently expose personally identifiable information. This apprehension limits the adoption of AI tools.

## Approach
- **Data analysis & requirements** – I evaluated common data fields covered by FERPA (student names, IDs, emails, phone numbers, Social Security Numbers, addresses) to determine what needed redaction.
- **Backend development** – I built a Python module (`ferpa_anonymizer.py`) that uses regular expressions and custom patterns to detect and redact those sensitive data types. A Flask API (`app.py`) exposes an `/anonymize` endpoint that returns the anonymized text plus statistics about the removed entities.
- **Frontend demo** – A lightweight HTML/JavaScript interface (`index.html`) allows users to paste text, call the API, and view the anonymized result alongside the summary of what was redacted.

## Outcomes
The tool reliably removes personally identifiable information, enabling administrators to safely use LLMs for analytics without exposing FERPA-protected data. By open-sourcing the code and documenting the workflow, I provide transparency and a starting point for other institutions. Future work includes incorporating NLP-based entity recognition, adding more robust evaluation metrics, and integrating the tool into existing data pipelines.
