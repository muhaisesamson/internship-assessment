import streamlit as st
import os
from backend.pipeline import process_input
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file  
st.write("TOKEN LOADED:", bool(os.getenv("SUNBIRD_API_TOKEN")))  # Debugging line to check if token is loaded

st.set_page_config(
    page_title="Sunbird Internship Assessment", 
    page_icon=":bird:", 
    layout="centered"
)

st.title("Sunbird Internship Assessment")

st.markdown("""
    upload audio or enter text for:
    speech-to-text transcription, text summarization, translation, and text-to-speech synthesis.
""")

st.sidebar.header("Configuration")

input_type = st.sidebar.selectbox(
    "Choose input type:", 
    ["audio", "text"]
)

target_language = st.sidebar.selectbox(
    "Choose target language for translation:", 
    [
    "Acholi",
    "English",
    "Igbo",
    "Lugbara",
    "Luganda",
    "Runyankole",
    "Swahili",
    "Ateso",
    "Lusoga",
    "Kinyarwanda",
    "Lumasaba",
    "Jopadhola",
    "Alur",
    "Bari",
    "Rukiga",
    "Lugwere",
    "Kumam",
    "Karamojong",
    "Kakwa",
    "Rukonjo",
    "Kupsabiny",
    "Lango",
    "Samia",
    "Aringa",
    "Ma'di",
    "Pokot",
    "Lugungu",
    "Ruruuli",
    "Kwamba",
    "Lubwisi",
    "Lunyole",
    "Runyoro"
    ]
)

result = None

if input_type == "text":
    text_input = st.text_area("Enter your text here:", height=200)
    
    if st.button("Process Text"):
        if text_input.strip() != "":
            with st.spinner("Processing..."):
                
                result = process_input(
                    input_type="text",
                    input_data=text_input,
                    target_language=target_language
                )
                st.write(result)

elif input_type == "audio":
    
    uploaded_file = st.file_uploader("Upload an audio file (mp3, wav, ogg):", type=["mp3", "wav", "ogg"])
    
    if st.button("Process Audio"):
        if uploaded_file is not None:
            
            temp_path = f"temp/{uploaded_file.name}"
            os.makedirs("temp", exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())
            with st.spinner("Processing..."):
                
                result = process_input(
                    input_type="audio",
                    input_data=temp_path,
                    target_language=target_language
                )
                
if result:
    
    st.success("Processing complete!")
    st.subheader("Original Text:")
    st.write(result.get("original_text", "N/A"))
    
    if result.get("transcript"):
        st.subheader("Transcription:")
        st.write(result.get("transcript", "N/A"))
    
    
    st.subheader("Summary:")
    st.write(result.get("summary", "N/A"))
    
    st.subheader("Translated Text:")
    st.write(result.get("translated_text", "N/A"))
    
    output_path = result.get("output_file_path")
    if output_path and os.path.exists(output_path):
        st.subheader("Synthesized Speech:")
        with open(output_path, "rb") as output_file:
            st.audio(output_file.read())