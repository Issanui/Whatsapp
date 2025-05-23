import streamlit as st
import pandas as pd
import pywhatkit
import time

st.set_page_config(page_title="Envoi WhatsApp", layout="centered")

st.title("📲 Envoi de messages WhatsApp en masse")

# Charger le fichier
uploaded_file = st.file_uploader("📤 Charger un fichier Excel avec une colonne 'Numéro' (format +223...)", type=["xlsx"])

# Zone de saisie du message
message = st.text_area("✍️ Message à envoyer", height=150)

# Bouton d'envoi
if uploaded_file and message:
    df = pd.read_excel(uploaded_file)
    
    if 'Numéro' not in df.columns:
        st.error("La colonne 'Numéro' est introuvable dans le fichier.")
    else:
        if st.button("🚀 Envoyer les messages"):
            st.success("Ouverture de WhatsApp Web...")
            for i, row in df.iterrows():
                numero = str(row['Numéro'])
                try:
                    st.write(f"📨 Envoi à {numero}")
                    pywhatkit.sendwhatmsg_instantly(numero, message, wait_time=10, tab_close=True)
                    time.sleep(10)
                except Exception as e:
                    st.error(f"Erreur avec {numero} : {e}")
            st.success("✅ Tous les messages ont été traités.")
else:
    st.info("Veuillez charger un fichier et écrire un message.")
