from django.shortcuts import render
from django.http import HttpResponse
import datetime


def main(request):
    now = datetime.datetime.now()
    morning = {'morning':'歡迎光臨，來杯提神的咖啡吧'}
    afternoon = {'afternoon':'歡迎光臨，來份下午茶吧'}
    if now.hour < 12:
        return render(request,'main/main.html', morning)
    else:
        return render(request,'main/main.html', afternoon)
# Create your views here.
