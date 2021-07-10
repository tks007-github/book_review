from django.urls import path
from django.urls.resolvers import URLPattern

from .import views


app_name = 'review'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('review-list/', views.ReviewListView.as_view(), name='review_list'),
]