import google.generativeai as genai

# Ide kell majd a kulcsod, amit a Google AI Studio-ból szerzel be
genai.configure(api_key="AIzaSyCsplqEmX63UapZ4fYpXRpGr5k-fk4UAok")
model = genai.GenerativeModel('gemini-1.5-flash')

# A te 300 IQ-s szabályod
rendszer_szabaly = "Te egy 300 IQ-s asszisztens vagy. Neved: Mentor300. Udvarias vagy, nem pofázol vissza. Gazdád: Botond."

print("--- Mentor300 Online ---")

while True:
    kerdes = input("Botond: ")
    if kerdes.lower() == "stop": break
    
    valasz = model.generate_content(kerdes)
    print(f"Mentor300: {valasz.text}")