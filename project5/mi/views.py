from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rohith(request):
    return render(request,'rohith.html')


def sky(request):
    return HttpResponse('<h1><marquee>he is the best 360 batsman</h1></marquee>')
