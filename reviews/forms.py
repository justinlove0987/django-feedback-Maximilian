from django import forms

class ReviewForm(forms.Form):
    # required validators is defaul.
    # https://docs.djangoproject.com/en/3.2/ref/forms/fields/
    user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a shorter name!"
    })
    # widget=forms.Textarea will render a textarea instead of the text input.
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)