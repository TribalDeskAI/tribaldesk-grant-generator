import streamlit as st
from docxtpl import DocxTemplate
import json

st.set_page_config(page_title="TribalDesk AI - Grant Chat", layout="centered")
st.title("🤖 TribalDesk AI - Grant Proposal Assistant")

# Load mock grants
with open("mock_grants.json", "r") as f:
    grant_data = json.load(f)

st.markdown("### 🔍 Available Grants")

selected_grant = st.selectbox("Select a Grant to Apply For:", options=[g['title'] for g in grant_data])

grant = next((g for g in grant_data if g['title'] == selected_grant), None)

if grant:
    st.markdown(f"**Deadline:** {grant['deadline']}")
    st.markdown(f"**Budget:** {grant['budget']}")
    st.markdown(f"**Summary:** {grant['summary']}")
    with st.expander("📋 View Grant Checklist"):
        st.markdown("\n".join([f"- {item}" for item in grant['checklist']]))

st.markdown("---")
st.markdown("### 💬 Fill Out Your Proposal")

org_name = st.text_input("Your Organization’s Name")
project_title = st.text_input("Project Title", value=grant['title'] if grant else "")
summary = st.text_area("Executive Summary", value=grant['summary'] if grant else "")
background = st.text_area("Organization Background")
problem = st.text_area("Problem Statement / Needs Assessment")
goals = st.text_area("Project Goals & Objectives")
methods = st.text_area("Methods / Project Design")
timeline = st.text_area("Timeline")
evaluation = st.text_area("Evaluation Plan")
budget = st.text_area("Budget Overview", value=grant['budget'] if grant else "")

if st.button("📄 Generate Proposal" and project_title):
    doc = DocxTemplate("template.docx")
    context = {
        "org_name": org_name,
        "project_title": project_title,
        "summary": summary,
        "background": background,
        "problem": problem,
        "goals": goals,
        "methods": methods,
        "timeline": timeline,
        "evaluation": evaluation,
        "budget": budget
    }
    doc.render(context)
    output_path = "generated_grant_proposal.docx"
    doc.save(output_path)
    
    with open(output_path, "rb") as file:
        st.success("✅ Grant Proposal Ready!")
        st.download_button(
            label="Download Grant Proposal",
            data=file,
            file_name="Grant_Proposal.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )