from django.http import HttpResponse


def say(request):
    return  HttpResponse("helloworld")
