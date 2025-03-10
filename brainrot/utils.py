import os
import pymupdf  


def extract_text(pdf_filename):
    BASE_DIR = os.path.dirname(__file__)
    pdf_path = os.path.join(BASE_DIR, "pdfs", pdf_filename)
    doc = pymupdf.open(pdf_path)  
    extracted_text = ""
    for page in doc:  
        extracted_text += page.get_text() + "\n"  
    return extracted_text

from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def summarize(extracted_text):
    client = OpenAI(api_key=api_key)
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate subtitles for short-form, engaging videos. Your response should be natural, short sentences like spoken language. Do NOT include titles, bullet points, or section headers."},
            {"role": "user", "content": f"Summarize and explain this text I provide you so to viewer learns as much as possible for a short-form video, making it engaging {extracted_text}"}
    ]   
    )
    completion_dict = completion.model_dump()
    generated_text = completion_dict["choices"][0]["message"]["content"]
    return generated_text
    



