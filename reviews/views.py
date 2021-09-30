from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

def review(request):
    # method property which tells us the HTTP method which was used for this request.
    if request.method == 'POST':
        # request.POST gives us access to the data itself. It will gives us a dictionary where the keys are the names set on the inputs in the form, and the value are the entered values.
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html")


# POST request is meant to subit data to the server not to get some page.
# instead of rendering a template, we redirect to a dirrent URL with a GET reuqest.
def thank_you(request):
    return render(request, "reviews/thank_you.html")