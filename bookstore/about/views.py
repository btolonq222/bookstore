from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'context':'我們是一家高品質的綜合性書店，不僅有豐富的藏書、優雅的環境，更有令人垂涎的咖啡與甜點，讓您沈浸在香味四溢的書香氣息環境中'}
    return render(request, 'about/about.html', context)
# Create your views here.
