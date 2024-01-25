from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Happening son \n <a href='/rango/about/'>Click here</a> to go back to the index page")


def about(request):
    return HttpResponse("Rango says here is the about page \n <a href='/rango/'>link text</a>")
