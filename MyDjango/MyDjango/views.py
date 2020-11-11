from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("<h1>Hello, DJango!</h1>")
def param(request):
    p = request.GET.get('msg')
    return HttpResponse("<h1>Hello, "+ p +"!</h1>")

def gohtml(request):
    p = request.GET.get('msg')
    context = {'msg' : p}
    return render(request, 'gohtml.html', context)
    