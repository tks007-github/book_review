from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

import review

from .models import Reiview
from review import models

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Reiview
    template_name = 'review_list.html'