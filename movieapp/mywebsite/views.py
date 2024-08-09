from django.shortcuts import render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
import requests



# Create your views here.
def commentpage(request):
    all_comments = models.Comment.objects.all()
    comment_dictionary = {"comments": all_comments}  # Sözlük olarak tanımlanmalı
    return render(request, 'mywebsite/commentpage.html', context=comment_dictionary)

@login_required(login_url="/login")
def addcomment(request):
    if request.method == "POST":
        # nickname yerine user instance'ı alıyoruz
        user = request.user  
        comment = request.POST["comment"]
        rating = request.POST["rating"]
        models.Comment.objects.create(user=user, comment_text=comment, rating=rating)
        return redirect(reverse('mywebsite:commentpage'))
    else:
        return render(request, 'mywebsite/addcomment.html')

@login_required
def deletecomment(request,id):
    comment = models.Comment.objects.get(pk=id)
    if request.user == comment.user:
        models.Comment.objects.filter(id=id).delete()
        return redirect("mywebsite:commentpage")
    


        
    
    


def whattowatch(request):
    return render(request,'mywebsite/whattowatch.html')





def intheaters(request):
    api_key = 'dc2cb6eba9dc7aa882ffe77d243ec2e3'
    base_url = 'https://api.themoviedb.org/3/movie/upcoming'
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    
    movies = []
    for page in range(1,3): 
        params['page'] = page
        response = requests.get(base_url, params=params)
        data = response.json()
        movies.extend(data.get('results', []))

    return render(request, 'mywebsite\inTheaters.html', {'movies': movies})
    



class signUpView(CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def imdb_top_100(request):
    api_key = 'dc2cb6eba9dc7aa882ffe77d243ec2e3'
    base_url = 'https://api.themoviedb.org/3/movie/top_rated'
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }
    
    movies = []
    for page in range(1, 6): 
        params['page'] = page
        response = requests.get(base_url, params=params)
        data = response.json()
        movies.extend(data.get('results', []))

    return render(request, 'mywebsite/imdbtop.html', {'movies': movies})