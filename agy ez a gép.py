import streamlit as st
import google.generativeai as genai

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Hiányzik a GEMINI_API_KEY!")

rendszerszabaly = (
    "Te egy végtelenül laza, közvetlen, baráti AI asszisztens vagy (mint egy haver). "
    "KIZÁRÓLAG magyarul válaszolhatsz, kivéve, ha a felhasználó kifejezetten megkér rá, hogy válts nyelvet! "
    "A stílusod legyen fiatalos, használj szlenget (pl. bro, geci, adom, darálás), ne legyél hivatalos vagy karót nyelt. "
    "A válaszaid legyenek rövidek, lényegretörőek és scannalhetőek. "
    "Mindig igazodj a felhasználó hangulatához és stílusához!"
)

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
    
    teljes_keres = f"{rendszerszabaly}\n\nFelhasználó kérdése: {user_query}"
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    with st.chat_message("assistant"):
        with st.spinner("Gondolkozom..."):
            try:
                response = model.generate_content(teljes_keres)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                hiba_szoveg = "Bocsi bro, túl gyorsan nyomtuk, a Google kért egy kis pihenőt. Nyomj rá mindjárt újra!"
                st.markdown(hiba_szoveg)
                st.session_state.messages.append({"role": "assistant", "content": hiba_szoveg})