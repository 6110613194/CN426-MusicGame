from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'games/index.html')

def play(request):
    return render(request,'games/play.html')

def score(request):
    return render(request,'games/score.html')
