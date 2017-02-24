from django.http import HttpResponse
from django.conf import settings
from django.http import Http404
from django.utils.html import escape
import json

def home(request):
    return HttpResponse("API HOME")

def fb_messages(request):
    if request.method == 'GET':
        return setup_webhook(request)
    elif request.method == 'POST':
        return parse_message(request)

def setup_webhook(request):
    mode = request.GET.get('hub.mode', '')
    verify_token = request.GET.get('hub.verify_token', '')
    challenge = request.GET.get('hub.challenge', '')
    if mode == 'subscribe' and verify_token == settings.FB_VERIFY_TOKEN:
        return HttpResponse(challenge)
    else:
        return HttpResponse("NOT FOUND", status=400)
    
def parse_message(request):
    
    data = ""
    sender_id = ""
    try:
        data = json.loads(request.body)['entry'][0]['messaging'][0]["message"]["text"]
        sender_id = json.loads(request.body)['entry'][0]['messaging'][0]["sender"]["id"]
    except:
        data = ""
        sender_id = ""

    print sender_id
    send_message_to_user(sender_id, "HELLO FROM ALIG")

    return HttpResponse(data)

def send_message_to_user(sender_id, message):
    json_data = {
        "recipient": {"id": sender_id},
        "message": {"text": message}
    }
    params = {
        "access_token": settings.FB_MESSENGER_ACCESS_TOKEN
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)
    print(r, r.status_code, r.text)