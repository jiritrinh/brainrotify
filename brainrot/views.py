from django.shortcuts import render
from .forms import PDFUploadForm
from .utils import extract_text

# Create your views here.
def homepage(request):
    extracted_text = None
    
    if request.method == 'POST':  
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_instance = form.save()
            pdf_path = pdf_instance.file.path
            extracted_text = extract_text(pdf_path)
    else:
        form = PDFUploadForm()
    return render(request, 'brainrot/home.html', {'form': form, 'text': extracted_text})
    
    
    