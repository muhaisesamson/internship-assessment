from backend.sunbird_client import (transcribe_audio, summarize_text, translate_text, text_to_speech)

def process_input(input_type, input_data, target_language):
    
    transcript = None
    
    if input_type == "audio":
        
        stt_result = transcribe_audio(input_data)
        
        if "error" in stt_result:
            return stt_result
        
        transcript = stt_result.get("transcript", "")
        
        original_text = transcript
        
    elif input_type == "text":
        
        original_text = input_data
        
    else:
        return {
            "error": "Invalid input type."
        }
        
    summary_result = summarize_text(original_text)
    
    if "error" in summary_result:
        return summary_result
    
    summary = summary_result.get("summary", "")
    
    
    translation_result = translate_text(summary, target_language)
    if "error" in translation_result:
        return translation_result
    
    translated_text = translation_result.get("translated_text", "")
    
    
    
    tts_result = text_to_speech(translated_text, target_language)
    if "error" in tts_result:
        return tts_result
    
    output_file_path = tts_result.get("output_file_path", "")
    
    return {
        "original_text": original_text,
        "transcript": transcript,
        "summary": summary,
        "translated_text": translated_text,
        "output_file_path": output_file_path
     }