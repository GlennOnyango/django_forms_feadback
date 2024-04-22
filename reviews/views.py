from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import views
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .forms import ReviewForm
from .models import Review
# Create your views here.


class reviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()

    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


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

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        loaded_review = self.object

        session_details = self.request

        session_review_id = session_details.session.get('fav_rev')

        context["is_favourite"] = session_review_id == str(loaded_review.id)

        return context


class reviewFavourite(views.View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['fav_rev'] = review_id
        return HttpResponseRedirect("/review/"+review_id)
