from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm


# Create your views here.

def review(request):
    # method property which tells us the HTTP method which was used for this request.
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # .is_valid() will validate the inputs
        if form.is_valid():
            # .cleaned_data is the field that will contain the cleaned validated data automatically.
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    # if we don't make the value into the if block above, we would recreate the form and rerender the template.
    form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


# POST request is meant to subit data to the server not to get some page.
# instead of rendering a template, we redirect to a dirrent URL with a GET reuqest.
def thank_you(request):
    return render(request, "reviews/thank_you.html")