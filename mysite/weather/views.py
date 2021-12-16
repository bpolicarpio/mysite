from django.shortcuts import render
from django.http import HttpResponse

from .models import Weather

# Create your views here.
def index(request):
    if request.method == "POST":
        if "feeling" in request.POST and "weather" in request.POST:
            feeling = request.POST["feeling"]
            weather = request.POST["weather"]
            if feeling == "happy":
                feeling = True
            else:
                feeling = False
            if weather == "good":
                weather = True
            else:
                weather = False

            Weather.objects.create(weather=weather, feeling=feeling)

            return HttpResponse(f"Feeling: {feeling}, Weather: {weather}")
        else:
            return render(request, "weather/index.html", {
                "message": "Please answer all questions."
            })

    return render(request, "weather/index.html")


