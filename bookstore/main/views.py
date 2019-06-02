from django.shortcuts import render
from django.http import HttpResponse
import datetime


def main(request):
    now = datetime.datetime.now()
    if now.hour < 12:
        return HttpResponse('歡迎光臨，來杯提神的咖啡吧')
    else:
        return HttpResponse('歡迎光臨，來份下午茶吧')
# Create your views here.
