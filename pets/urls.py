# pets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.pet_list, name="pet_list"),
    path("add/", views.add_pet, name="add_pet"),
    path("vote/<int:pet_id>/", views.vote_pet, name="vote_pet"),
    path("winner/", views.winner, name="winner"),
]
