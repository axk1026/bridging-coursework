from django.urls import path
from . import views
from .models import CV

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('CV', views.CV_list, name='CV_list'),
    path('CV/<int:pk>/', views.CV_detail, name='CV_detail'),
    path('CV_list', views.CV2_list, name='CV2_list'),
    path('CV2/<int:pk>/', views.CV2_detail, name='CV2_detail'),
    path('CV/<int:pk>/edit/', views.CV_edit, name='CV_edit'),
    path('CV/new/', views.CV_new, name='CV_new'),
    #used for testing

]
