import streamlit as st
import json
from docxtpl import DocxTemplate
from io import BytesIO

st.set_page_config(page_title="Grant Finder + Proposal Generator", layout="centered")
st.title("🧩 TribalDesk AI - Select Grant & Generate Proposal")

with open("grants_data.json", "r") as f:
    grants = json.load(f)

selected = st.selectbox("Select a Grant to Auto-Fill:", [g['title'] for g in grants])

grant = next(g for g in grants if g['title'] == selected)

st.markdown(f"### {grant['title']}")
st.markdown(f"**Agency:** {grant['agency']}")
st.markdown(f"**Summary:** {grant['summary']}")

notes = st.text_area("Additional Notes / Custom Info")

if st.button("Generate Proposal Document"):
    doc = DocxTemplate("proposal_template.docx")
    context = {
        "title": grant['title'],
        "summary": grant['summary'],
        "agency": grant['agency'],
        "notes": notes
    }
    output = BytesIO()
    doc.render(context)
    doc.save(output)
    output.seek(0)
    st.success("Proposal document is ready!")
    st.download_button("Download Proposal", data=output, file_name="Auto_Filled_Proposal.docx")