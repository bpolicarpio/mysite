from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Weather
import matplotlib.pyplot as plt

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

            return redirect('weather:results')

        else:
            return render(request, "weather/index.html", {
                "message": "Please answer all questions."
            })

    return render(request, "weather/index.html")

def results(request):
    results = Weather.objects.all()
    happy, sad, good, bad = 0, 0, 0, 0
    for result in results:
        if result.weather is True:
            good += 1
        else:
            bad += 1
        if result.feeling is True:
            happy += 1
        else:
            sad +=1

    weatherX = ['good', 'bad']
    weatherY = [good, bad]
    plt.bar(weatherX, weatherY)
    plt.title('Weather')
    plt.xlabel('weather')
    plt.ylabel('quantity')
    plt.savefig('/weather/static/weath.png')

    feelingX = ['happy', 'sad']
    feelingY = [happy, sad]
    plt.bar(feelingX, feelingY)
    plt.title('Feeling')
    plt.xlabel('feeling')
    plt.ylabel('quantity')
    plt.savefig('/weather/static/feel.png')

    return render(request, 'weather/results.html')
