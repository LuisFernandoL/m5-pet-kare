from django.urls import path
from .views import PetView, PetsDetailView

urlpatterns = [
    path("pets/", PetView.as_view()),
    path("pets/<int:pet_id>/", PetsDetailView.as_view())           
    ]
