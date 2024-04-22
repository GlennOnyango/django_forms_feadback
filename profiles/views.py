from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileModel

from django.views.generic import CreateView, ListView

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = ProfileModel
    fields = "__all__"
    success_url = "/profiles"


class UserProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    model = ProfileModel
    context_object_name = "profiles"