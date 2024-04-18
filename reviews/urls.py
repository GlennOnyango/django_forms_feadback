from django.urls import path
from . import views


urlpatterns = [
    path("", views.reviewView.as_view()),
    path("thank-you",views.thankYouView.as_view()),
    path("reviews",views.reviewsList.as_view()),
    path("review/<int:pk>",views.reviewDisplay.as_view()),
]
