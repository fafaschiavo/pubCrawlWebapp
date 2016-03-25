from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("AAAAW Yes! This is Pub Crawl App Motherfucker!")