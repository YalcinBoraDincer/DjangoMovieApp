from django.shortcuts import render
from . import models

# Create your views here.
def commentpage(request):
    all_comments = models.Comment.objects.all()
    comment_dictionary = {"comments",all_comments}
    return render(request,'mywebsite/commentpage.html',context=comment_dictionary)

def addcomment(request):
    
    return render(request,'mywebsite/addcomment.html')


def whattowatch(request):
    return render(request,'mywebsite/whattowatch.html')


def imdbtops(request):
    return render(request,'mywebsite/imdbtop.html')


def intheaters(request):
    return render(request,'mywebsite/intheaters.html')


