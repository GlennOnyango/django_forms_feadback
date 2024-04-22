from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import ProfileModel

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        profile_form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": profile_form})

    def post(self, request):
        submited_form = ProfileForm(request.POST, request.FILES)

        if submited_form.is_valid():
            profile_model = ProfileModel(image=request.FILES["image"])
            profile_model.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {"form": submited_form})
