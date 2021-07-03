from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class HomeOverview(ListView):

    model = models.HomeOverview
    template_name = 'home/overview.html'
    context_object_name = 'homeoverview'