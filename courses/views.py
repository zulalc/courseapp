from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (req):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurs listesi')  