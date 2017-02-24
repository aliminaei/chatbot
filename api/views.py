from django.http import HttpResponse
from django.conf import settings
from django.http import Http404

def home(request):
    return HttpResponse("API HOME")

def fb_messages(request):
    if request.method == 'GET':
        setup_webhook(request)
    elif request.method == 'POST':
        parse_message(request)

def setup_webhook(request):
    mode = request.GET.get('hub.mode', '')
    verify_token = request.GET.get('hub.verify_token', '')
    challenge = request.GET.get('hub.challenge', '')
    if mode == 'subscribe' and verify_token == settings.FB_VERIFY_TOKEN:
        return HttpResponse(challenge)
    else:
        return HttpResponse("NOT FOUND", status=400)
    
def parse_message(request):
    return HttpResponse("DONE!!!")