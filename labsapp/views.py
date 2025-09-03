from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

# Create your views here.

def landing_page(request):
    return render(request, 'labsapp/landing_page.html')

def download_windows(request):
    """Serve the 100labs.exe located at project root as an attachment."""
    exe_path = os.path.join(settings.BASE_DIR, '100labs.exe')
    if not os.path.exists(exe_path):
        raise Http404("Installer not found")
    response = FileResponse(open(exe_path, 'rb'), as_attachment=True, filename='100labs.exe')
    return response