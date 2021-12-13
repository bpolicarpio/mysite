from django.shortcuts import render
from django.http import HttpResponse
from .forms import WeatherForm

# Create your views here.
def index(request):
    form = WeatherForm
    return render(request, "weather/index.html", {
        "form": form
    })


