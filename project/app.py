import gradio as gr
from backend.pipeline import process_input


LANGUAGES = [
    "Acholi", "English", "Igbo", "Lugbara", "Luganda",
    "Runyankole", "Swahili", "Ateso", "Lusoga",
    "Kinyarwanda", "Lumasaba", "Jopadhola", "Alur",
    "Bari", "Rukiga", "Lugwere", "Kumam",
    "Karamojong", "Kakwa", "Rukonjo", "Kupsabiny",
    "Lango", "Samia", "Aringa", "Ma'di",
    "Pokot", "Lugungu", "Ruruuli", "Kwamba",
    "Lubwisi", "Lunyole", "Runyoro"
]


def handle_audio(audio_file, target_language):

    if audio_file is None:
        return "No file uploaded", "", "", "", None

    result = process_input(
        input_type="audio",
        input_data=audio_file,
        target_language=target_language
    )

    return (
        result.get("original_text", "N/A"),
        result.get("transcript", "N/A"),
        result.get("summary", "N/A"),
        result.get("translated_text", "N/A"),
        result.get("output_file_path", None)
    )


def handle_text(text_input, target_language):

    if not text_input.strip():
        return "No text entered", "", "", "", None

    result = process_input(
        input_type="text",
        input_data=text_input,
        target_language=target_language
    )

    return (
        result.get("original_text", "N/A"),
        result.get("transcript", "N/A"),
        result.get("summary", "N/A"),
        result.get("translated_text", "N/A"),
        result.get("output_file_path", None)
    )


theme = gr.themes.Soft()

with gr.Blocks(theme=theme, title="Sunbird AI Multimodal App") as demo:

    gr.Markdown("""
    # 🌍 Sunbird AI Multimodal Application

    Transform text or speech into summarized, translated, and spoken content using Sunbird AI APIs.

    ### Features
    - 🎤 Speech-to-Text Transcription
    - 📝 AI Summarization
    - 🌐 Translation into Ugandan Local Languages
    - 🔊 AI Text-to-Speech Synthesis

    ### How to Use
    1. Choose a target language
    2. Upload audio OR enter text
    3. Click process
    4. View and listen to results
    """)

    with gr.Row():

        language = gr.Dropdown(
            choices=LANGUAGES,
            value="English",
            label="🌐 Select Target Language",
            interactive=True
        )

    with gr.Tabs():

        # AUDIO TAB
        with gr.Tab("🎤 Audio Processing"):

            gr.Markdown(
                "Upload an audio recording for transcription, summarization, translation, and speech synthesis."
            )

            audio_input = gr.Audio(
                type="filepath",
                label="Upload Audio File"
            )

            audio_button = gr.Button(
                "Process Audio",
                variant="primary"
            )

            with gr.Accordion("📄 Results", open=True):

                original_output = gr.Textbox(
                    label="Original Text"
                )

                transcript_output = gr.Textbox(
                    label="Transcription"
                )

                summary_output = gr.Textbox(
                    label="Summary"
                )

                translated_output = gr.Textbox(
                    label="Translated Text"
                )

                speech_output = gr.Audio(
                    label="Synthesized Speech"
                )

            audio_button.click(
                handle_audio,
                inputs=[audio_input, language],
                outputs=[
                    original_output,
                    transcript_output,
                    summary_output,
                    translated_output,
                    speech_output
                ]
            )

        # TEXT TAB
        with gr.Tab("📝 Text Processing"):

            gr.Markdown(
                "Enter text to summarize, translate, and generate speech."
            )

            text_input = gr.Textbox(
                lines=8,
                label="Enter Text"
            )

            text_button = gr.Button(
                "Process Text",
                variant="primary"
            )

            with gr.Accordion("📄 Results", open=True):

                text_original = gr.Textbox(
                    label="Original Text"
                )

                text_transcript = gr.Textbox(
                    label="Transcription"
                )

                text_summary = gr.Textbox(
                    label="Summary"
                )

                text_translation = gr.Textbox(
                    label="Translated Text"
                )

                text_audio = gr.Audio(
                    label="Synthesized Speech"
                )

            text_button.click(
                handle_text,
                inputs=[text_input, language],
                outputs=[
                    text_original,
                    text_transcript,
                    text_summary,
                    text_translation,
                    text_audio
                ]
            )

demo.launch(server_name="127.0.0.1", server_port=7860)