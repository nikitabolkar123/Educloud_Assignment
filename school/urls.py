from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('school/listing/', views.school_listing, name='school_listing'),
    path('school/create/', views.create_school, name='create_school'),
   ]