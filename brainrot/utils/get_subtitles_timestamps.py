from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
BASE_DIR = os.path.dirname(__file__)

def timestamp_audio(audio_name):
    audio_file_path = Path(__file__).parent / "speech.mp3"

    audio_file= open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="verbose_json",
        timestamp_granularities=["word"]
    )
    return transcription.words


def format_timestamp(seconds):
    hours = int(seconds // 3600)  
    minutes = int((seconds % 3600) // 60)  
    secs = int(seconds % 60)  
    milliseconds = int((seconds % 1) * 1000)  
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"

def convert_to_srt(transcription, output_file = os.path.join(BASE_DIR, "source_for_video", "subtitles.srt")):
    with open(output_file, "w", encoding="utf-8") as file:
        for index, word in enumerate(transcription, 1):
            start = format_timestamp(word.start)
            end = format_timestamp(word.end)
            w = word.word
            file.write(f"{index}\n{start} --> {end}\n{w}\n\n")   
    
    

     
    