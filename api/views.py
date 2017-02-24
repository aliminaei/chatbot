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
    data = json.loads(request.body).entry[0].messaging[0].message.text
    print data


        # {
        #     "object":"page",
        #     "entry":[
        #         {
        #             "messaging":[
        #                 {
        #                     "message":{
        #                         "text":"does this work?",
        #                         "seq":20,
        #                         "mid":"mid.1466015596912:7348aba4de4cfddf91"
        #                     },
        #                     "timestamp":1466015596919,
        #                     "sender":{
        #                         "id":"885721401551027"
        #                     },
        #                     "recipient":{
        #                         "id":"260317677677806"
        #                     }
        #                 }
        #             ],
        #             "time":1466015596947,
        #             "id":"260317677677806"
        #         }
        #     ]
        # }


    return HttpResponse("body")