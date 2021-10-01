from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


# Create your views here.

def review(request):
    # method property which tells us the HTTP method which was used for this request.
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # When form.save(), we will then save the data not as a new entry,- 
        # - but to update the existing entry in the database.
        existing_data = Review.objects.get(pk=1)
        form = ReviewForm(request.Post, instance=existing_data)
        # .is_valid() will validate the inputs
        if form.is_valid():
            # if we use modelform we can skip the step, we don't need to create our model instance.
            # review = Review(
            #     user_name=form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating = form.cleaned_data['rating'])
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")

    # if we don't make the value into the if block above, we would recreate the form and rerender the template.
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


# POST request is meant to subit data to the server not to get some page.
# instead of rendering a template, we redirect to a dirrent URL with a GET reuqest.
def thank_you(request):
    return render(request, "reviews/thank_you.html")