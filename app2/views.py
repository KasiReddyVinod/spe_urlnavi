from django.shortcuts import render

# Create your views here.
def mom (request):
    return render(request,'mom.html')
def dad (request):
    return render (request,'dad.html')
