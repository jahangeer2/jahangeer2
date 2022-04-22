from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def testing1(request):
    print("hello1")
    return render(request, 'index.html')


def XYZ(request):
    print("hello xyz")
    return HttpResponse("hello this is my xyz request")
