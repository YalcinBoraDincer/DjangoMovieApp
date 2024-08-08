from django.shortcuts import render

# Create your views here.
def commentpage(request):
    return render(request,'mywebsite/commentpage.html')

def whattowatch(request):
    return render(request,'mywebsite/whattowatch.html')


def imdbtops(request):
    return render(request,'mywebsite/imdbtop.html')


def intheaters(request):
    return render(request,'mywebsite/intheaters.html')


