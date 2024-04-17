from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label="Your Name", error_messages={
#         "required": "Please fill the empty username field",
#         "max_length": "Text length exceeded"
#     })

#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea)

#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your rating"
        }
        error_message = {
            "user_name": {
                "required": "Please fill the empty username field",
                "max_length": "Text length exceeded"
            },
        }
