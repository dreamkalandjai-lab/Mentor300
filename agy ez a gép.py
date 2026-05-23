import streamlit as st
import google.generativeai as genai

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Hiányzik a GEMINI_API_KEY!")

st.title("🧠 Mentor300")
st.write("A stabil, újratöltött asszisztens")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Írj ide valamit..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    with st.chat_message("assistant"):
        with st.spinner("Gondolkozom..."):
            try:
                response = model.generate_content(user_query)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Várj egy kicsit, a Google pihen!")