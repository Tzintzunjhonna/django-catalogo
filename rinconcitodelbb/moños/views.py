from django.shortcuts import render
from .models import Moño

# Create your views here.


def moños(request):
    moños = Moño.objects.all()
    return render(request, "moños/moños.html", {'moños': moños})