from django.shortcuts import render

# Create your views here.
def leaderboard(request):
    context = {'leaderboard': "Wellcome To Todo List from Jinja2 this your about page"}
    return render(request, 'leaderboard.html', context)