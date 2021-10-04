from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })

class TankYouView(TemplateView):
    def get_template_names(self):
        return ["reviews/thank_you.html"]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Good Job!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    # django will fetch all the data realted to the model -
    # - and pass it as context to the template.
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    # django automatically took the model name basically all lower case - 
    # - and exposes the fetched single peice of data though the model name to our template.
    model = Review
    
    # django identify a single item with our slug or the primary key defined by us in our urls.py.