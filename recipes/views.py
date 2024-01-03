from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta, timezone


def horas():
    fuso = timezone(timedelta(hours=-3))
    hora_br = datetime.now(fuso)
    if 0 == hora_br.hour < 12:
        return 'Bom dia'
    elif 12 > hora_br.hour < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite' 

def home(request):    
    return render(request, 'recipes/pages/home.html', context= {
        'name': 'Diego!',
        'periodo': horas()
    })
