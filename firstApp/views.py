from django.shortcuts import render, redirect
from . import models
from . import forms;

# Create your views here.


def index(request):
    return render(request, "firstApp/index.html")


def games(request):
    games = models.Games.objects.all();
    return render(request, "firstApp/games.html",{'games': games}); 
def game_detail(request, game_id):
    game = models.Games.objects.get(id=game_id)
    game_genres = game.genre.all()
    print(game_genres)
    return render(request, "firstApp/game_detail.html", {'game': game, 'game_genres': game_genres})

def info(request):
    if request.method == "POST":
        form = forms.DetailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            # return render(request, "firstApp/info_success.html", {
            #     'name': name,
            #     'age': age,
            #     'email': email,
            #     'address': address,
            # })
            return redirect("info_success", name=name, age=age, email=email, address=address);
        
            
        
    else:
        form = forms.DetailForm()
    return render(request, "firstApp/info.html", {'form': form})
    
    
def info_success(request,name,age, email, address):
    # print(name,age,email,address)
    return render(request, "firstApp/info_success.html", {
        'name': name,
        'age': age,
        'email': email,
        'address': address,
    })
    

def model_form_info(request):
    if request.method == "POST":
        form = forms.DetailModelForm(request.POST)
        if form.is_valid():
            detail_instance = form.save()
            return redirect("info_success", name=detail_instance.name, age=detail_instance.age, email=detail_instance.email, address=detail_instance.address);
    else:
        form = forms.DetailModelForm()
    return render(request, "firstApp/model_form_info.html", {'form': form})