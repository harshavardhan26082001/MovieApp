from django.shortcuts import render
import json
import requests

# Create your views here.

def welcome(request):
    response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=56db406e58392c2ff59a312e7368fc82')
    data = response
    return render(request,"welcome.html",{'data':data})