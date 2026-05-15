# Sunbird AI Multimodal GenAI Application

## Project Description

 This application is a multimodal AI system that processes either text or audio input. It transcribes audio (if provided), summarizes the content using Sunbird’s Sunflower LLM, translates the summary into selected Ugandan local languages, and generates speech output using Sunbird’s Text-to-Speech API. The final output includes the original text, summary, translated text, and playable audio.

## Architecture Overview

  Input (Text / Audio via Gradio UI)  
             ↓  
  Speech-to-Text (Sunbird STT API)  
             ↓  
  Summarization (Sunflower LLM)  
             ↓  
  Translation (Sunflower LLM)  
             ↓  
  Text-to-Speech (Sunbird TTS API)  
             ↓  
  Gradio UI Output (Text + Audio Player)


## Tech Stack

  Python
  -Gradio (Frontend)
  -Requests (API calls)
  -Sunbird AI APIs:
    .Speech-to-Text
    .Sunflower LLM (Summarization & Translation)
    .Text-to-Speech
    
## UI Framework

This project was migrated from Streamlit to Gradio for improved file upload handling, faster UI rendering, and better compatibility with Hugging Face Spaces deployment as Streamlit file upload function was colliding with Hugging Face Spaces security setups and permission was being denied.

## Project Structure

project/
│
├── app.py (Gradio entry point)
├── backend/
│   ├── pipeline.py
│   ├── sunbird_client.py
│
├── requirements.txt
├── .env
├── .env.example
└── README.md

## Environment Variables

  SUNBIRD_API_TOKEN
      -API key for authenticating with Sunbird services

## Setup Instructions

git clone <repo-url>
cd internship-assessment

python -m venv venv
source venv/Scripts/activate  # Windows

pip install -r requirements.txt

python app.py

## Usage Instructions

  -Open the app in browser
  -Choose input type:
  -Text or Audio
  -If audio, upload file (≤ 5 minutes)
  -Select target language:
      .Luganda / Runyankole / Ateso / Lugbara / Acholi
  -Click “Process”
  -View:
      .Original text
      .Summary
      .Translation
      .Audio output (playable)

# Deployment Link

https://huggingface.co/spaces/muhaisesamson/Sunbird_AI




