from flask import Flask, request, jsonify
from ferpa_anonymizer import anonymize_text
import os

app = Flask(__name__)

@app.route("/anonymize", methods=["POST"])
def anonymize():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    anonymized, stats = anonymize_text(text)
    return jsonify({"anonymized": anonymized, "stats": stats})

if __name__ == "__main__":
    app.run(debug=True)
