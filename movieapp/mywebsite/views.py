import random
from tokenize import Comment
from django.shortcuts import get_object_or_404, render,redirect
from . import models
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
import requests
from .models import Comment




# Create your views here.
def commentpage(request):
    all_comments = Comment.objects.all()  # Comment modelini kullanıyoruz
    comment_dictionary = {"comments": all_comments}
    return render(request, 'mywebsite/commentpage.html', context=comment_dictionary)


@login_required
def addcomment(request, movie_id):
    if request.method == "POST":
        user = request.user
        comment = request.POST["comment"]
        rating = request.POST["rating"]
        Comment.objects.create(user=user, comment_text=comment, rating=rating, movie_id=movie_id)
        return redirect(reverse('mywebsite:commentpage'))
    else:
        return render(request, 'mywebsite/addcomment.html', {'movie_id': movie_id})




@login_required
def deletecomment(request,id):
    comment = models.Comment.objects.get(pk=id)
    if request.user == comment.user:
        models.Comment.objects.filter(id=id).delete()
        return redirect("mywebsite:commentpage")
        
def whattowatch(request):
    api_key = 'dc2cb6eba9dc7aa882ffe77d243ec2e3'
    base_url = 'https://api.themoviedb.org/3/movie/'

    def get_random_movie():
        randomID = random.randint(1, 10000)
        params = {
            'api_key': api_key,
            'language': 'en-US',
        }
        response = requests.get(base_url + str(randomID), params=params)
        movie = response.json()
        
        if response.status_code == 200 and movie.get('status_code') is None and movie.get('poster_path'):
            return movie
        return None

    movie = None
    while movie is None:
        movie = get_random_movie()

    return render(request, 'mywebsite/whattowatch.html', {'movie': movie})

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
    

def movieinfo(request,id):
    movie_id = id
    api_key = 'dc2cb6eba9dc7aa882ffe77d243ec2e3'  
    base_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'api_key': api_key,
        'language': 'en-US',
    }
    
    response = requests.get(base_url, params=params)
    movie = response.json()
    print(movie)

    return render(request, 'mywebsite/movieinfo.html', {'movie': movie})


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