import os 
import requests
import mimetypes
from dotenv import load_dotenv

load_dotenv()

SUNBIRD_API_TOKEN = os.getenv("SUNBIRD_API_TOKEN")
BASE_URL = "https://api.sunbird.ai"

def send_request(endpoint, files=None, data=None, json=None):
    url = f"{BASE_URL}/{endpoint}"
    
    headers = {
        "Authorization": f"Bearer {SUNBIRD_API_TOKEN}"
    }
    try:
        response = requests.post(
            url,     
            headers=headers, 
            files=files, 
            data=data, 
            json=json
        )
        
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Show the actual error from the API
        if hasattr(e, 'response') and e.response is not None:
            return {
                "error": str(e),
                "status_code": e.response.status_code,
                "api_response": e.response.text
            }
        return {"error": str(e)}
    
def transcribe_audio(audio_file_path, language='eng'):
    with open(audio_file_path, 'rb') as audio_file:
        
        file_content = audio_file.read()
        print(f"DEBUG: File size = {len(file_content)} bytes")
        print(f"DEBUG: File not empty = {len(file_content) > 0}")
        audio_file.seek(0)  # Reset file pointer back to beginning
        
        filename = os.path.basename(audio_file_path)
        
        mime_type, _ = mimetypes.guess_type(audio_file_path)
        if not mime_type:
            # Default for common audio files
            if filename.endswith('.ogg'):
                mime_type = 'audio/ogg'
            elif filename.endswith('.mp3'):
                mime_type = 'audio/mpeg'
            elif filename.endswith('.wav'):
                mime_type = 'audio/wav'
            else:
                mime_type = 'application/octet-stream'
        
        files = {
            "audio": (filename, file_content, mime_type)
        }
        
        # Send language parameter
        form_data = {
            "language": language
        }
        
        result = send_request(
            endpoint="tasks/stt",
            files=files,
            data=form_data
        )
        
        if "error" in result:
            return result
        
        # Extract the transcription
        transcript = result.get("audio_transcription", "")
        
        return {
            "transcript": transcript,
            "detected_language": result.get("language", language),
            "transcription_id": result.get("audio_transcription_id"),
            "was_trimmed": result.get("was_audio_trimmed", False)
        }
        
        



def summarize_text(text):
    
    prompt = f"""Provide a concise summary of the text.
    
    Text: 
    {text}    
    """     
    payload = {
        "text": text
    }
    
    result = send_request(
        endpoint="tasks/summarise",
        json=payload
    ) 
    if "error" in result:
        return result
    
    try:
        summary = result.get("summarized_text", "No summary available")
         
        return {
            "summary": summary
        }
    
    except Exception as e:
        return {
            "error": f"Failed to parse summary response: {str(e)}",
            "raw_response": result
        }
    
    
def translate_text(text, target_language):
    
    prompt = f"""
            Translate the following text to {target_language}:
            Text:
            {text}    
    """
    
    result = send_request(
        endpoint="tasks/sunflower_simple",
        data={  # Use 'data' not 'json' for form-urlencoded
            "instruction": prompt,
            "model_type": "qwen",  # optional
            "temperature": 0.3  # lower temp for more accurate translation
        }
        # Do NOT set Content-Type: application/json header
    )
    
    print("DEBUG RESPONSE:", result)
        
    try:
        translated_text = (
            result.get("response")
            or result.get("output", {}).get("content")
            or result.get("content")
            or result.get("result")
            or "No translation available"
        )
        
        return {
            "translated_text": translated_text,
            "target_language": target_language
        }
        
    except Exception as e:
        return {
            "error": f"Failed to parse translation response: {str(e)}",
            "raw_response": result
        }
        
    
    
def text_to_speech(text, language, output_file_path="temp/output_audio.ogg"):
    
    url = f"{BASE_URL}/tasks/tts"
    
    headers = {
        "Authorization": f"Bearer {SUNBIRD_API_TOKEN}"
    }
    
    payload = {
        "text": text,
        "language": language
    }
    
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )
        
        response.raise_for_status()
        
        
        with open(output_file_path, 'wb') as output_file:
            output_file.write(response.content)
            
        return {
            "output_file_path": output_file_path
        }
        
    except requests.exceptions.RequestException as e:
        
        if hasattr(e, 'response') and e.response is not None:
            return {
                "error": str(e),
                "status_code": e.response.status_code,
                "api_response": e.response.text
            }
        return {"error": str(e)}