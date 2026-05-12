# Sunbird AI Multimodal GenAI Application

## Project Description

 This application is a multimodal AI system that processes either text or audio input. It transcribes audio (if provided), summarizes the content using Sunbird’s Sunflower LLM, translates the summary into selected Ugandan local languages, and generates speech output using Sunbird’s Text-to-Speech API. The final output includes the original text, summary, translated text, and playable audio.

         
## Architecture Overview

  Input (Text / Audio Upload)
          ↓
  Speech-to-Text (if audio)
          ↓
  Summarization (Sunflower LLM)
          ↓
  Translation (Sunflower LLM)
          ↓
  Text-to-Speech (TTS API)
          ↓
  Output Display (Streamlit UI)

## Tech Stack

  Python
  -Streamlit (Frontend)
  -Requests (API calls)
  -Sunbird AI APIs:
    .Speech-to-Text
    .Sunflower LLM (Summarization & Translation)
    .Text-to-Speech

## Project Structure

  project/
  │
  ├── streamlit_app.py
  ├── backend/
  │   ├── pipeline.py
  │   ├── sunbird_client.py
  │
  ├── temp/
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
  source venv/Scripts/activate   # Windows
  pip install -r requirements.txt
  
  streamlit run streamlit_app.py

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





