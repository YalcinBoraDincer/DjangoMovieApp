from django.shortcuts import render,redirect
from . import models
from django.urls import reverse

# Create your views here.
def commentpage(request):
    all_comments = models.Comment.objects.all()
    comment_dictionary = {"comments",all_comments}
    return render(request,'mywebsite/commentpage.html',context=comment_dictionary)

def addcomment(request):
    if request.method == "POST":
        nickname = request.POST["nickname"]
        comment = request.POST["comment"]
        rating = request.POST["rating"]
        #movie = models.Movie.objects.get(id=movie_id)
        models.Comment.objects.create(nickname = nickname,comment_text=comment, rating=rating)
        return redirect(reverse('mywebsite:commentpage'))
    else:
        return render(request, 'mywebsite/addcomment.html')

        
    
    


def whattowatch(request):
    return render(request,'mywebsite/whattowatch.html')


def imdbtops(request):
    return render(request,'mywebsite/imdbtop.html')


def intheaters(request):
    return render(request,'mywebsite/intheaters.html')


