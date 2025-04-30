import streamlit as st
import json

st.set_page_config(page_title="Grant Finder", layout="centered")
st.title("📚 TribalDesk AI - Grant Search + Checklist Tool")

with open("grants_data.json", "r") as f:
    grants = json.load(f)

search_term = st.text_input("Search by keyword (e.g. 'tribal', 'education')").lower()

filtered = [g for g in grants if search_term in g['title'].lower() or search_term in g['summary'].lower()] if search_term else grants

for grant in filtered:
    with st.expander(grant['title']):
        st.markdown(f"**Agency:** {grant.get('agency', 'N/A')}")
        st.markdown(f"**Summary:** {grant['summary']}")