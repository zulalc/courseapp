from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (req):
    return HttpResponse('anasayfa')

def hakkimizda(request):
    return HttpResponse('hakkımızda') 

def iletisim(request):
    return HttpResponse('iletişim')