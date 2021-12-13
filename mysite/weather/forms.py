from django import forms

class WeatherForm(forms.Form):
    CHOICES = [("Foggy","foggy"), ("Mostly Foggy", "mostly foggy")]
    weather = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="How's the weather today?")