# AI Contract Analyzer

This project extracts and classifies clauses from contracts using Python, Flask, and NLP techniques.

## Features:
- Reads and processes multiple PDF contracts.
- Extracts key clauses like Confidentiality, Indemnification, Termination.
- Provides an API endpoint for analysis.

## Installation

1. Clone this repository:
  git clone https://github.com/ayampandey/AI-Contract-Analyzer.git
2. Navigate to the folder:
   cd AI-Contract-Analyzer
3. Create a virtual environment:
  python -m venv venv
4. Activate the environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
  pip install -r requirements.txt

 ## Running the Flask App
 ## Using the API in Postman

1. Open [Postman](https://www.postman.com/).
2. Make a **POST request** to:
   http://127.0.0.1:5000/analyze_folder
3. Select "Body" → "form-data" → Add a **key** called `file` and upload a contract PDF.
4. Click "Send" to get the extracted clauses.
