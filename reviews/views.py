from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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


class ReviewsListView(TemplateView):
    def get_template_names(self):
        return ["reviews/review_list.html"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class SingleReviewView(TemplateView):
    def get_template_names(self):
        return ["reviews/single_review.html"]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # id is from urls.py
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context