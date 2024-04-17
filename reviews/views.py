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
            clean_data = form.cleaned_data
            review = Review(
                user_name=clean_data["user_name"],
                review_text=clean_data["review_text"],
                rating=clean_data["rating"])
            
            review.save()

            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
