from django.urls import path
from . import views 

app_name = 'teams' # Help with namespacing

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('<int:team_id>/', views.team_detail, name='team_detail'),
    path('players/', views.my_player_list, name='banana'),
    path('new/', views.new_team, name='new_team'),
    path('create/', views.create_team, name='create_team')
]