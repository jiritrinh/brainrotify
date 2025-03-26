from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = api_key)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def text_to_audio(text, audio_file_name):
    speech_file_path = os.path.join(BASE_DIR, "source_for_video", audio_file_name)
    response = client.audio.speech.create(
        model="tts-1",
        voice="ash",
        input= text,
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path

    
