from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player
from .forms import TeamForm

# Create your views here.
def team_list(request):
    # Get all the teams from the DB
    teams = Team.objects.all().order_by('name')
    context = {
        'teams': teams
    }
    return render(request, 'teams/index.html', context)

def team_detail(request, team_id):
     # Get a single Team object by its ID, or raise a 404 error if not found
    team =  get_object_or_404(Team, pk=team_id)

    # The 'related_name' 'players' allows us to access all players related to this team
    context = {
        'team': team,
    }
    return render(request, 'teams/team_detail.html', context)
    # players = team.players.all().order_by('last_name') # Already accessible in template via team.players.all

def my_player_list(request):
    players = Player.objects.all().order_by('last_name', 'first_name')
    context = {
        'players': players
    }
    return render(request, 'teams/player_list.html', context)

def new_team(request):

    # Check for the HTTP request type
    # If it's POST then insert a new team
    # Else render the form

    form = TeamForm()

    context = {
        'new_team_form': form
    }

    return render(request, 'teams/new_team.html', context)

def create_team(request):
    # Create a new Team based on the Form content
    new_team = TeamForm(request.POST)
    # Check if it's valid
    if new_team.is_valid():
          # Save to DB
        new_team.save()
         # redirect the browser
        return redirect('teams:team_list')
  
   
    