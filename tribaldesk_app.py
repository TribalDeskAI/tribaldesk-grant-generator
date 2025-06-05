from openai import OpenAI

def chat_assistant():
    st.title("🧠 TribalDeskAI Chat Assistant")
    st.write("Ask a question about grants, proposals, tribal funding, or startup support.")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", placeholder="Ask me anything...")

    if user_input:
        # Add user's message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Call OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.chat_history
            )

            assistant_reply = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            assistant_reply = f"⚠️ Error: {str(e)}"
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

    # Display the conversation
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Assistant:** {msg['content']}")

