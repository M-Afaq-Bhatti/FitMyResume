import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from analyzer import calculate_similarity

st.title("🧠 Resume Analyzer for Job Fit Scoring")

job_desc = st.text_area("Paste the Job Description here", height=200)

uploaded_files = st.file_uploader("Upload Resume PDFs", type="pdf", accept_multiple_files=True)

if st.button("Analyze"):
    if not job_desc:
        st.warning("Please enter a job description.")
    else:
        scores = []
        for file in uploaded_files:
            resume_text = extract_text_from_pdf(file)
            score = calculate_similarity(resume_text, job_desc)
            scores.append((file.name, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        st.subheader("📊 Resume Fit Scores")
        for name, score in scores:
            st.write(f"**{name}** — Score: {round(score*100, 2)}%")
