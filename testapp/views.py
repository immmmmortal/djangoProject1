from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def testapp(request: HttpRequest) -> HttpResponse:
    return render(request, 'testapp.html')
