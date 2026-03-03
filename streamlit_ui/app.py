import streamlit as st

from ai_agent.code_quality_checker import CodeQualityChecker

st.title("AI Agent - Code Quality Checker")
code = st.text_area("Source Code", height=300)
checklist = st.text_area("Checklist", value="SOLID\nError handling\nLogging\nSecurity")

if st.button("Run Review"):
    checker = CodeQualityChecker()
    result = checker.review(code, checklist)
    st.markdown("### Observations & Suggestions")
    st.write(result)
