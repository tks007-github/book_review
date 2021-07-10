from django.urls import path
from django.urls.resolvers import URLPattern

from .import views


app_name = 'review'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name='index'),
    path('review-list/', views.ReviewListView.as_view(), name='review_list'),
    path('review-detail/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('review-create/', views.ReviewCreateView.as_view(), name='review_create'),
]