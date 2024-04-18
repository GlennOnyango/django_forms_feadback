from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
from .models import Review
# Create your views here.


class reviewView(views.View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


class thankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        context["message"] = "Thank you for working with us"

        return context


class reviewsList(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review

    context_object_name = "reviews"

    # def get_queryset(self):
    #     superQuery = super().get_queryset()
        
    #     return superQuery.filter(rating__gt=3)


class reviewDisplay(DetailView):
    template_name = "reviews/review_display.html"
    model = Review

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)

    #     review_id = kwargs["review_id"]
    #     review = Review.objects.get(pk=review_id)

    #     context["review"] = review

    #     return context
