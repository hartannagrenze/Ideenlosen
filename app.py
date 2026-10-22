import streamlit as st
import json
import random

datenbank_json = """
{
    "INTERAKTION": [
        "KURBELN", "PUSTEN", "ZIELEN", "SCHREIEN", "SCHLAGEN", 
        "WERFEN", "BERÜHREN", "STREICHELN", "QUETSCHEN", "HÜPFEN", 
        "TANZEN", "ZIEHEN", "KRATZEN"
    ],
    "SPIELART": [
        "SINNFREI", "SCHUMMEL", "RÄTSEL", "LOGIK", "TEAM", 
        "1 v 1", "GLÜCK", "ROLLE", "SOLO", "GRUPPE", 
        "KREATIV", "SAMMELN", "SABOTAGE"
    ],
    "AUSGABE": [
        "pfeifen", "Sound", "Mini-Drucker", "LEDs", "Projektion", 
        "Temperatur", "Bildschirm", "3D-Druck", "eigenes Gerät", 
        "Vibration", "Impulse / Stromschläge", "Bewegung"
    ],
    "MATERIAL": [
        "PAPIER", "LATEX", "SAND", "Schleim", "Schnüre", 
        "Kabelbinder", "Pferdehaare", "Stein", "METALL", 
        "Flüßigkeit", "Organismus", "HOLZ", "PLASTE", "KNETE"
    ],
    "Sensorik": [
        "TEMPERATUR", "FLEX", "JOYSTICK", "KAMERA", "MIKROFON", 
        "KNOPF", "DISTANZ", "MAGNET", "PULS", "FADER / POTI", "MÄUSE"
    ]
}
"""

kategorien = json.loads(datenbank_json)

st.title("🎲 IDEENLOSEN – Zufallsgenerator")
st.write("Klicke auf den Button, um eine neue Kombination zu generieren!")

if st.button("Neue Kombination ziehen"):
    st.markdown("---")
    for kategorie, woerter in kategorien.items():
        auswahl = random.choice(woerter).upper()
        st.markdown(f"### **{kategorie.upper()}**: `{auswahl}`")