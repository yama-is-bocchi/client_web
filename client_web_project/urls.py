from django.urls import path
from client_web_project import views

app_name = 'client_web_project'
urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.start_game, name='start_game'),
    path('game2/', views.start_eng_game, name='start_eng_game'),
]