import streamlit as st
import json

st.set_page_config(page_title="Real-Time Grant Finder", layout="centered")
st.title("🌐 TribalDesk AI - Real-Time Federal Grant Finder")

st.markdown("This tool displays the latest federal grants from Grants.gov using live data (via RSS).")

with open("realtime_grants.json", "r") as f:
    grants = json.load(f)

search_term = st.text_input("Search by keyword (e.g. 'tribal', 'education')").lower()

filtered_grants = [g for g in grants if search_term in g['title'].lower() or search_term in g['summary'].lower()] if search_term else grants

for grant in filtered_grants:
    with st.expander(grant['title']):
        st.markdown(f"**Published:** {grant['published']}")
        st.markdown(f"**Agency:** {grant.get('agency', 'N/A')}")
        st.markdown(f"**Summary:** {grant['summary']}")
        st.markdown(f"[🔗 View Grant Opportunity]({grant['link']})", unsafe_allow_html=True)