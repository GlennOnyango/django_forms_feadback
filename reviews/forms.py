from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Your Name", error_messages={
        "required": "Please fill the empty username field",
        "max_length": "Text length exceeded"
    })

    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=1, min_length=5)

    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
