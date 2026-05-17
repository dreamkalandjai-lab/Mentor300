import streamlit as st
import google.generativeai as genai

# API kulcs beállítása a Streamlit Secrets-ből
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Hiányzik a GEMINI_API_KEY a Secrets beállításokból!")

# Modell inicializálása
model = genai.GenerativeModel('gemini-1.5-flash')

# Webes felület címe
st.title("🧠 Mentor300")
st.write("A 300 IQ-s asszisztens")

# Chat előzmények kezelése
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eddigi üzenetek kirajzolása a képernyőre
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Felhasználói adatbevitel (Webes chat mező)
if prompt := st.chat_input("Írj valamit a Mentor300-nak..."):
    # Felhasználó üzenetének megjelenítése és mentése
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI válasz generálása
    with st.chat_message("assistant"):
        with st.spinner("Gondolkozom..."):
            teljes_kerdes = f"Rendszerszabály: Te egy 300 IQ-s asszisztens vagy. Neved: Mentor300. Üzenet: {prompt}"
            response = model.generate_content(teljes_kerdes)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})