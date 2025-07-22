import re
import os

def anonymize_text(text):
    stats = {
        "names": 0,
        "ids": 0,
        "phones": 0,
        "emails": 0,
        "ssns": 0,
        "addresses": 0
    }

    def redact_names(text):
        pattern = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')
        return pattern.sub(lambda m: f"Student", text), len(pattern.findall(text))

    def redact_ids(text):
        pattern = re.compile(r'\b(?:ID|Student ID|ID#):\s*\d+')
        return pattern.sub("ID: [REDACTED]", text), len(pattern.findall(text))

    def redact_phones(text):
        pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')
        return pattern.sub("XXX-XXX-XXXX", text), len(pattern.findall(text))

    def redact_emails(text):
        pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        return pattern.sub("email@redacted.com", text), len(pattern.findall(text))

    def redact_ssn(text):
        pattern = re.compile(r'\b\d{3}-?\d{2}-?\d{4}\b')
        return pattern.sub("XXX-XX-XXXX", text), len(pattern.findall(text))

    def redact_address(text):
        pattern = re.compile(r'\b\d+\s+[A-Za-z\s]+(?:Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd)\b')
        return pattern.sub("[ADDRESS REDACTED]", text), len(pattern.findall(text))

    text, stats["names"] = redact_names(text)
    text, stats["ids"] = redact_ids(text)
    text, stats["phones"] = redact_phones(text)
    text, stats["emails"] = redact_emails(text)
    text, stats["ssns"] = redact_ssn(text)
    text, stats["addresses"] = redact_address(text)

    return text, stats

def anonymize_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    anonymized, stats = anonymize_text(content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(anonymized)

    return stats

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FERPA Anonymizer CLI")
    parser.add_argument("input", help="Path to the input .txt file")
    parser.add_argument("output", help="Path to save the anonymized .txt file")

    args = parser.parse_args()

    result_stats = anonymize_file(args.input, args.output)
    print("Anonymization complete. Stats:")
    for k, v in result_stats.items():
        print(f"{k}: {v}")
