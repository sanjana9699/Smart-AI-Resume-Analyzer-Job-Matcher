import streamlit as st
from utils import extract_text_from_pdf, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 Smart AI Resume Analyzer & Job Matcher")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description")

if st.button("Analyze"):
    if resume_file and job_description:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            result = analyze_resume(resume_text, job_description)
            
            st.header("🔍 Match Score")
            st.metric(label="Resume vs Job Description", value=f"{result['score']}%")
            
            st.header("🧩 Missing Keywords")
            missing_keywords = ", ".join(result["missing_keywords"]) or "None 🎉"
            st.markdown(
                f"""
                <div style="
                    background-color: #fffbcc;  /* soft yellow */
                    color: #333333;             /* dark text */
                    padding: 15px; 
                    border-radius: 8px; 
                    max-height: 150px; 
                    overflow-y: auto;
                    font-weight: 600;
                    font-size: 14px;
                    line-height: 1.4;
                ">
                    {missing_keywords}
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.header("✍️ GPT-4 Suggestions")
            with st.expander("Click to expand suggestions"):
                st.write(result["suggestions"])
    else:
        st.warning("Please upload a resume and paste the job description.")
