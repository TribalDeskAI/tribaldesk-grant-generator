import streamlit as st
from openai import OpenAI

# === Page Setup ===
st.set_page_config(page_title="TribalDeskAI", layout="wide")

# === Sidebar Navigation ===
st.sidebar.title("TribalDeskAI")
page = st.sidebar.selectbox("Choose a tool", [
    "🧠 Chat Assistant", 
    "📝 Proposal Generator", 
    "🔍 Grant Finder"
])

# === Chat Assistant Function ===
def chat_assistant():
    st.title("🧠 TribalDeskAI Chat Assistant")
    st.write("Ask me anything about grants, proposals, tribal funding, or startups.")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", placeholder="How can I help you today?")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.chat_history
            )
            reply = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
        except Exception as e:
            reply = f"⚠️ Error: {str(e)}"
            st.session_state.chat_history.append({"role": "assistant", "content": reply})

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Assistant:** {msg['content']}")

# === Placeholder Functions for Other Tools ===
def proposal_generator():
    st.title("📝 Grant Proposal Generator")
    st.info("This tool will soon generate customized grant proposals.")

def grant_finder():
    st.title("🔍 Grant Finder Tool")
    st.info("This tool will search for active federal, foundation, and tribal grants.")

# === Page Routing Logic ===
if page == "🧠 Chat Assistant":
    chat_assistant()
elif page == "📝 Proposal Generator":
    proposal_generator()
elif page == "🔍 Grant Finder":
    grant_finder()
