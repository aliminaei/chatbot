from django.http import HttpResponse
from django.conf import settings
from django.http import Http404

def home(request):
    return HttpResponse("API HOME")