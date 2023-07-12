# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.landing_page, name='landing_page'),
#     # path('school/listing/', views.school_listing, name='school_listing'),
#     path('search/', views.search_schools, name='search_schools'),
#     path('school/list/', views.school_list, name='school_list'),
# ]
from django.urls import path
from . import views
from .views import create_school
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('school/listing/', views.school_listing, name='school_listing'),
    path('school/create/', views.create_school, name='create_school'),
    # path('login', views.UserLogin.as_view(), name='login'),
   ]