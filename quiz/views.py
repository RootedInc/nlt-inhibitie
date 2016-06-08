from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
import time, requests

# Create your views here.
def index(request):
    request.session.clear()
    request.session["amans"] = 0
    request.session["gamans"] = 0
    request.session["completed"] = False
    return render(request, 'app/index.html')

prevcolour = None
def kleurtest(request):
    global prevcolour
    time_started = request.session.get("time_started")
    amans = request.session.get("amans")
    gamans = request.session.get("gamans")
    completed = request.session.get("completed")
    
    if (amans is None) or (gamans is None) or (completed is None):
        return redirect("index")
    
    if time_started is None:
        time_started = time.time()
        request.session["time_started"] = time_started

    if int(time.time() - time_started) >= 60:
        request.session["completed"] = True
        return redirect("resultaten")

    if (request.method == "POST"):
        amans += 1
        request.session["amans"] = amans
        uinput = request.POST.get("antwoord", None)
        if uinput is not None:
            if uinput.lower() == prevcolour:
                gamans += 1
                request.session["gamans"] = gamans

    kleurind = randint(1, 5)
    if kleurind == 1:
        prevcolour = "zwart"
    elif kleurind == 2:
        prevcolour = "rood"
    elif kleurind == 3:
        prevcolour = "groen"
    elif kleurind == 4:
        prevcolour = "blauw"
    elif kleurind == 5:
        prevcolour = "geel"

    kleurtxt_ind = randint(1, 5)
    if kleurtxt_ind == 1:
        kleurtxt = "Zwart"
    elif kleurtxt_ind == 2:
        kleurtxt = "Rood"
    elif kleurtxt_ind == 3:
        kleurtxt = "Groen"
    elif kleurtxt_ind == 4:
        kleurtxt = "Blauw"
    elif kleurtxt_ind == 5:
        kleurtxt = "Geel"
        
    
    return render(request, 'app/kleurtest.html', {'kleur': "kleur-" + str(kleurind), 'kleurtext': kleurtxt})
    
def resultaten(request):
    amans = request.session.get("amans")
    gamans = request.session.get("gamans")
    completed = request.session.get("completed")
    
    if completed == False:
        return redirect("index")
    else:
        if amans <= 10:
            request.session["notnuff"] = True
            return redirect("notnuff")
        score = "Zeg hoeveel je er hebt geantwoord en hoeveel je er goed had."
        return render(request, 'app/resultaten.html', {'amans': amans, 'gamans': gamans, 'score': str(score)})
        
def notnuff(request):
    if request.session.get("notnuff"):
        return render(request, 'app/notnuff.html', {})
    else:
        return redirect("index")