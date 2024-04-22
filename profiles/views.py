from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileModel

from django.views.generic import CreateView

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = ProfileModel
    fields = "__all__"
    success_url = "/profiles"
