import streamlit as st
import google.generativeai as genai

# API kulcs beállítása
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Hiányzik a GEMINI_API_KEY a Secrets beállításokból!")

# Modell inicializálása
model = genai.GenerativeModel('gemini-2.5-flash')

st.title("🧠 Mentor300")
st.write("A 300 IQ-s asszisztens (Most már van memóriája!)")

# Chat előzmények kezelése Streamlitben
if "messages" not in st.session_state:
    st.session_state.messages = []

# Régi üzenetek kirajzolása a képernyőre
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Felhasználói üzenet fogadása
if user_query := st.chat_input("Írj valamit a Mentor300-nak..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # Átalakítjuk az előzményeket a Gemini számára megfelelő formátumba
    gemini_history = []
    for msg in st.session_state.messages:
        role_name = "user" if msg["role"] == "user" else "model"
        gemini_history.append({"role": role_name, "parts": [msg["content"]]})
    
    # Elindítjuk a chatet az eddigi memóriával és a rendszerszabállyal
    rendszerszabaly = "Te egy 300 IQ-s asszisztens vagy. Ne magadról pofázz folyton, hanem válaszolj pontosan, értelmesen és röviden a kérdésekre!"
    chat = model.start_chat(history=gemini_history)
    
    # Mentjük a felhasználó mostani üzenetét a Streamlit memóriába
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    # Válasz generálása
    with st.chat_message("assistant"):
        with st.spinner("Gondolkozom..."):
            response = chat.send_message(f"{rendszerszabaly}\n\nFelhasználó: {user_query}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})