from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InquiryForm, ReviewCreateForm

import review

from .models import Reiview
from review import models

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm

class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Reiview
    template_name = 'review_list.html'
    paginate_by = 3

    def get_queryset(self):
        reviews = Reiview.objects.filter(user=self.request.user).order_by('-created_at')
        return reviews

class ReviewDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Reiview
    template_name = 'review_detail.html'

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Reiview
    template_name = 'review_create.html'
    form_class = ReviewCreateForm
    success_url = reverse_lazy('review:review_list')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.save()
        messages.success(self.request, 'レビューを作成しました。')
        return super().form_valid(form)
    
    def form_valid(self, form):
        messages.error(self.request, 'レビューの作成に失敗しました。')
        return super().form_invalid(form)