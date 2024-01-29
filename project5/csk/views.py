from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')


def jadeja(request):
    return HttpResponse('<h1><marquee>he is the best spin bowler</h1></marquee>')