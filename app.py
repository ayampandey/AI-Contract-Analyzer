# from flask import Flask, request, jsonify
# import fitz
# import re
# import os
# import glob
#
# app = Flask(__name__)
#
# clause_patterns = {
#     "confidentiality": r"(confidentiality|non-disclosure|nda)",
#     "indemnification": r"(indemnify|hold harmless)",
#     "termination": r"(terminate|termination)",
# }
#
#
# def extract_clauses(text, patterns):
#     """Extract clauses based on predefined patterns."""
#     extracted_clauses = {}
#     for clause, pattern in patterns.items():
#         matches = re.findall(pattern, text, re.IGNORECASE)
#         if matches:
#             extracted_clauses[clause] = matches
#     return extracted_clauses
#
#
# def extract_text_from_folder(folder_path):
#     """Extract text from all PDFs in the given folder and subfolders."""
#     all_clauses = {}
#
#     # Use glob to find all PDF files in the folder and its subfolders
#     pdf_files = glob.glob(os.path.join(folder_path, "**/*.pdf"), recursive=True)
#
#     # Iterate through each PDF file, extract text, and analyze clauses
#     for pdf_file in pdf_files:
#         print(f"Processing {pdf_file}...")
#         # Extract text from the PDF
#         doc = fitz.open(pdf_file)
#         text = ""
#         for page in doc:
#             text += page.get_text("text") + "\n"
#
#         # Extract clauses from the text
#         clauses = extract_clauses(text, clause_patterns)
#         if clauses:
#             all_clauses[pdf_file] = clauses
#
#     return all_clauses
#
#
# @app.route("/analyze", methods=["POST"])
# def analyze_contract():
#     folder_path = r"C:\Users\hp\Downloads\CUAD\CUAD_v1\full_contract_pdf"  # Path to the folder containing PDFs
#     clauses = extract_text_from_folder(folder_path)
#
#     # Return the extracted clauses as JSON
#     return jsonify({"extracted_clauses": clauses})
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

import os
import fitz  # PyMuPDF
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define clause patterns for extraction
clause_patterns = {
    "confidentiality": r"(confidentiality|non-disclosure|nda)",
    "indemnification": r"(indemnify|hold harmless)",
    "termination": r"(terminate|termination)",
}


# Function to extract text from all PDFs in a folder
def extract_text_from_folder(folder_path):
    extracted_texts = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                text = extract_text(pdf_path)
                extracted_texts[file] = text

    return extracted_texts


# Function to extract text from a single PDF
def extract_text(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    return text


# Function to extract clauses from text
def extract_clauses(text, patterns):
    extracted_clauses = {}
    for clause, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            extracted_clauses[clause] = matches
    return extracted_clauses


# Flask route to analyze all PDFs in a folder
@app.route("/analyze_folder", methods=["POST"])
def analyze_folder():
    folder_path = request.json.get("folder_path")  # Folder path sent via JSON

    if not folder_path or not os.path.exists(folder_path):
        return jsonify({"error": "Invalid or missing folder path"}), 400

    pdf_texts = extract_text_from_folder(folder_path)
    clause_results = {}

    for file_name, text in pdf_texts.items():
        clause_results[file_name] = extract_clauses(text, clause_patterns)

    return jsonify({"results": clause_results})


if __name__ == "__main__":
    app.run(debug=True)