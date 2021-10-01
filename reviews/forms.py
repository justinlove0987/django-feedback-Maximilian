from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     # required validators is defaul.
#     # https://docs.djangoproject.com/en/3.2/ref/forms/fields/
#     user_name = forms.CharField(label="Your Name", max_length=10, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     # widget=forms.Textarea will render a textarea instead of the text input.
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    # let Django know which model the form is related.
    class Meta:
        model = Review
        # tells Django all properties should also receive fields in the form.
        fields = '__all__'
        # exclude = ['owner_comment']

