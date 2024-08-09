from django.urls import path
from.import views

app_name = 'mywebsite'

urlpatterns = [
    path('',views.imdbtops,name='imdbtops'),#bora.com/mywebsite/commentpage
    path('whattowatch/',views.whattowatch,name='whattowatch'),#bora.com/mywebsite/movies
    path('comentpage/',views.commentpage,name='commentpage'),#bora.com/mywebsite/commentpage
    path('intheaters/',views.intheaters,name='intheaters'),#bora.com/mywebsite/intheaters
    path('addcomment/',views.addcomment,name='addcomment'),#bora.com/mywebsite/addcomment
    path('signup/',views.signUpView.as_view(),name="signup"),
    
    
    
    
    
   
]
