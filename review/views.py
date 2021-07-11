from django import forms
from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm, ReviewCreateForm
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from review import models

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('review:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleane_data['name']))
        return super().form_valid(form)

class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = 'review_list.html'
    paginate_by = 3

    def get_queryset(self):
        reviews = Review.objects.filter(user=self.request.user).order_by('-created_at')
        return reviews

class ReviewDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'review_detail.html'

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewCreateForm
    success_url = reverse_lazy('review:review_list')

    def form_valid(self, form):
        review = form.save(commit=False)
        review.user = self.request.user
        review.save()
        messages.success(self.request, 'レビューを作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'レビューの作成に失敗しました。')
        return super().form_invalid(form)

class ReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    template_name = 'review_update.html'
    form_class = ReviewCreateForm

    def get_success_url(self):
        return reverse_lazy('review:review_detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, 'レビューを更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'レビューの更新に失敗しました。')
        return super().form_invalid(form)

class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('review:review_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'レビューを削除しました。')
        return super().delete(request, *args, **kwargs)
