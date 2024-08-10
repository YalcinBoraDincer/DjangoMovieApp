from django.urls import path
from.import views

app_name = 'mywebsite'

urlpatterns = [
    path('',views.imdb_top_100,name='imdbtop'),#bora.com/mywebsite/commentpage
    path('whattowatch/',views.whattowatch,name='whattowatch'),#bora.com/mywebsite/movies
    path('comentpage/',views.commentpage,name='commentpage'),#bora.com/mywebsite/commentpage
    path('intheaters/',views.intheaters,name='intheaters'),#bora.com/mywebsite/intheaters
    path('addcomment/<int:movie_id>/', views.addcomment, name='addcomment'),#bora.com/mywebsite/addcomment
    path('signup/',views.signUpView.as_view(),name="signup"),
    path('deletecomment/<int:id>',views.deletecomment,name="deletecomment"),
    path("movieinfo/<int:id>",views.movieinfo,name = "movieinfo"),
    
    
    
    
    
    
   
]
