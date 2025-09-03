from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
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

def lottie_scene(request):
    """Serve lottie.json (preferred) or scene.json from project root for Lottie."""
    candidate_names = ['lottie.json', 'Lottie.json', 'scene.json', 'Scene.json']
    for filename in candidate_names:
        json_path = os.path.join(settings.BASE_DIR, filename)
        if os.path.exists(json_path):
            with open(json_path, 'rb') as f:
                data = f.read()
            return HttpResponse(data, content_type='application/json')
    raise Http404("Animation not found")

def contact_submit(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    from_email = request.POST.get('fromEmail', '').strip()
    message = request.POST.get('message', '').strip()
    to_email = getattr(settings, 'CONTACT_TO_EMAIL', settings.EMAIL_HOST_USER)
    if not message or not from_email:
        return JsonResponse({'error': 'Missing fields'}, status=400)
    subject = f"100Labs inquiry from {from_email}"
    body = f"From: {from_email}\n\n{message}"
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [to_email])
        return JsonResponse({'ok': True})
    except BadHeaderError:
        return JsonResponse({'error': 'Invalid header'}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Send failed'}, status=500)