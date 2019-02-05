from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    return render(request, 'jquerydj/index.html', {'movies': movie})
