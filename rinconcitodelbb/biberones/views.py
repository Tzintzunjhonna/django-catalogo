from django.shortcuts import render
from .models import Biberon
# Create your views here.

def biberones(request):
    biberones = Biberon.objects.all()
    collapse = 'collapse'
    return render(request, "biberones/biberones.html", {'biberones': biberones, 'collapse': collapse})