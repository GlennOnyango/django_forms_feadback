from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

from .models import Review

# Create your views here.


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
