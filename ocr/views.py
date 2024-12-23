from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image

def ocr_view(request):
    extracted_text = ""
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.url(filename)
        
        # Perform OCR using Tesseract
        img = Image.open(fs.path(filename))
        extracted_text = pytesseract.image_to_string(img)
        
        return render(request, 'ocr/ocr_result.html', {
            'file_path': file_path,
            'extracted_text': extracted_text
        })
    return render(request, 'ocr/ocr_upload.html')
