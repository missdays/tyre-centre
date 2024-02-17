from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_mainpage(request):
    return render(request, 'mainpage/index.html')