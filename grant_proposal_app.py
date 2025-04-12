import streamlit as st
from docxtpl import DocxTemplate

st.title("Grant Proposal Generator")

project_name = st.text_input("Enter project name")
project_description = st.text_area("Enter project description")

if st.button("Generate Proposal"):
    doc = DocxTemplate("template.docx")
    context = {
        "project_name": project_name,
        "project_description": project_description
    }
    doc.render(context)
    output_path = "generated_proposal.docx"
    doc.save(output_path)
    
    with open(output_path, "rb") as file:
        st.download_button(
            label="Download Proposal",
            data=file,
            file_name="Grant_Proposal.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )