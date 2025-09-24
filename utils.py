import pdfplumber
import openai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

openai.api_key = "your-openai-key"
def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def get_match_score(resume_text, job_text) -> float:
    tfidf = TfidfVectorizer().fit_transform([resume_text, job_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)

def get_missing_keywords(resume_text, job_text) -> list:
    job_keywords = set(job_text.lower().split())
    resume_keywords = set(resume_text.lower().split())
    return list(job_keywords - resume_keywords)

def get_gpt_suggestions(resume_text, job_text) -> str:
    prompt = f"""
Compare the following resume and job description.
Give 3 suggestions to improve the resume so it better matches the job.

Resume:
{resume_text}

Job Description:
{job_text}
"""
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for resume analysis."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def analyze_resume(resume_text, job_text):
    return {
        "score": get_match_score(resume_text, job_text),
        "missing_keywords": get_missing_keywords(resume_text, job_text),
        "suggestions": get_gpt_suggestions(resume_text, job_text)
    }
