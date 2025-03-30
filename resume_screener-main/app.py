import streamlit as st
from utils.pdf_extractor import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume

st.title("AI Resume Screener & ATS Checker")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Enter Job Description")

if st.button("Check Resume Score"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume(job_description, resume_text)
        st.success("Analysis Complete!")
        st.text_area("Results", result, height=200)
    else:
        st.warning("Please upload a resume and enter a job description.")

if st.button("Predict for New Resume"):
    st.experimental_rerun()
