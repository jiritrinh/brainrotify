from django.shortcuts import render
from .forms import PDFUploadForm
from .utils.extract_text_from_pdf import extract_text
from .utils.summarize import summarize
from .utils.text_to_audio import text_to_audio
from .utils.get_subtitles_timestamps import timestamp_audio, convert_to_srt
from .utils.create_video import create_video

# Create your views here.
def homepage(request):
    final_text = None
    speech = None
    audio_name = "speech.mp3"
    transcription_words = None
    
    
    
    if request.method == 'POST':  
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_instance = form.save()
            pdf_path = pdf_instance.file.path
            
            # creating text summarization from chat open ai
            extracted_text = extract_text(pdf_path)
            final_text = summarize(extracted_text)
            
            # creating audio and subtitles file from open ai text
            speech = text_to_audio(final_text, audio_name)
            transcription_words = timestamp_audio(speech)
            convert_to_srt(transcription_words)
            
            
            
            
    else:
        form = PDFUploadForm()
    return render(request, 'brainrot/home.html', {'form': form, 'text': final_text})
    
    
    