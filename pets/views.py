from django.shortcuts import render, redirect, get_object_or_404
from .models import Pet
from .forms import PetForm

def pet_list(request):
    pets = Pet.objects.order_by("-votes", "name")
    return render(request, "pets/pet_list.html", {"pets": pets})

def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetForm()
    return render(request, "pets/add_pet.html", {"form": form})

def vote_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.votes += 1
    pet.save()
    return redirect("pet_list")

def winner(request):
    pets = Pet.objects.order_by("-votes")
    winner_pet = pets[0] if pets else None
    return render(request, "pets/winner.html", {"winner": winner_pet})
