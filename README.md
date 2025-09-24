📄 Smart AI Resume Analyzer & Job Matcher

A Streamlit-based web app that uses AI and NLP to analyze resumes and match them with job descriptions. It scores the match, identifies missing keywords, and provides GPT-4 powered suggestions to improve the resume.

🚀 Features

✅ PDF Resume Parsing

🧠 Match Score using TF-IDF & Cosine Similarity

🔍 Missing Keywords Detection

🤖 GPT-4 Suggestions to Improve Resume

🎯 Simple Streamlit Interface

📸 Demo

🧰 Tech Stack

Streamlit

pdfplumber

OpenAI GPT-4 API

scikit-learn

Python 3.7+

⚙️ Installation

Clone the repository

git clone https://github.com/sanjana9699/resume-analyzerSmart-AI-Resume-Analyzer.git
cd resume-analyzer


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Set your OpenAI API Key

Replace the API key directly in the code (not recommended for production):

openai.api_key = "your-openai-api-key"


For better security, use environment variables:

export OPENAI_API_KEY="your-openai-api-key"


Then in code:

import os
openai.api_key = os.getenv("OPENAI_API_KEY")

🧪 How to Use

Run the Streamlit app:

streamlit run app.py


Upload your resume PDF.

Paste the job description in the text area.

Click Analyze.

View:

✅ Match Score

🧩 Missing Keywords

✍️ GPT-4 Suggestions for improvement

📂 Project Structure
resume-analyzer/
│
├── app.py                  # Streamlit frontend
├── utils.py                # Resume analysis logic      
└── README.md               # This file

📌 To-Do

 Add keyword highlighting in resume

 Add LinkedIn Job scraping support

 Enhance keyword extraction using NLP (e.g., RAKE, spaCy)

 Export improved resume suggestions to a file

🛡️ Disclaimer

This project is for educational purposes and does not guarantee job placement or 100% accurate resume evaluation. GPT-4 suggestions may vary.
