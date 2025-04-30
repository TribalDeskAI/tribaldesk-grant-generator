import streamlit as st
import json

st.set_page_config(page_title="Grant Finder + Checklist", layout="centered")
st.title("📚 TribalDesk AI - Grant Search + Checklist Tool")

# Load simulated grant data
with open("grants_data.json", "r") as f:
    grants = json.load(f)

# Searchable dropdown
grant_titles = [g['title'] for g in grants]
selected = st.selectbox("Select a grant to view details:", grant_titles)

# Show grant info
if selected:
    grant = next(g for g in grants if g['title'] == selected)
    st.markdown(f"### {grant['title']}")
    st.markdown(f"**Deadline:** {grant['deadline']}")
    st.markdown(f"**Funding Range:** {grant['budget']}")
    st.markdown(f"**Summary:** {grant['summary']}")

    with st.expander("📋 Checklist of Requirements"):
        st.markdown("\n".join([f"- {item}" for item in grant['checklist']]))

    with st.expander("✅ Suggested Content to Include in Proposal"):
        st.markdown("\n".join([f"- {tip}" for tip in grant['tips']]))