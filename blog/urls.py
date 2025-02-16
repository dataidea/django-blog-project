from django.contrib import admin
from django.urls import path
from .views import home, details, about, contact

urlpatterns = [
   path(route='', view=home),
   path(route='<int:id>', view=details),
   path(route='about/', view=about),
   path(route='contact/', view=contact)
]
