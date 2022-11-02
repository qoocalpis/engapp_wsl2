import imp
from django.http import HttpResponse

def helloworldfunc(request):
    return HttpResponse('Hello World')